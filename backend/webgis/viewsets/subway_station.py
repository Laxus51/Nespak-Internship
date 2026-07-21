from rest_framework import viewsets
from ..models import NycSubwayStation
from ..serializers import NycSubwayStationSerializer


from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import Point
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance


class NycSubwayStationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NycSubwayStation.objects.all()
    serializer_class = NycSubwayStationSerializer

    @action(detail=False, methods=["get"])
    def bbox(self, request):

        xmin = request.query_params.get("xmin")
        ymin = request.query_params.get("ymin")
        xmax = request.query_params.get("xmax")
        ymax = request.query_params.get("ymax")

        # Check that all parameters exist
        if not all([xmin, ymin, xmax, ymax]):
            return Response(
                {"error": "xmin, ymin, xmax and ymax are required."},
                status=400
            )

        # Convert strings to floats
        try:
            xmin = float(xmin)
            ymin = float(ymin)
            xmax = float(xmax)
            ymax = float(ymax)
        except ValueError:
            return Response(
                {"error": "Coordinates must be numeric values."},
                status=400
            )

        # Create the bounding box
        bbox = Polygon.from_bbox((xmin, ymin, xmax, ymax))
        bbox.srid = 26918

        stations = NycSubwayStation.objects.filter(
            geom__intersects=bbox
        )

        serializer = self.get_serializer(stations, many=True)

        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def nearest(self, request):

        x = request.query_params.get("x")
        y = request.query_params.get("y")

        # Check that all parameters exist
        if not all([x, y]):
            return Response(
                {"error": "x and y are required."},
                status=400
            )
        
        # Convert strings to floats
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            return Response(
                {"error": "Coordinates must be numeric values."},
                status=400
            )

        # Create a point from the coordinates
        point = Point(x, y, srid=26918)

        # Find the nearest subway station
        nearest_station = (
            NycSubwayStation.objects
            .annotate(distance=Distance("geom", point))
            .order_by("distance")
            .first()
        )

        if not nearest_station:
            return Response(
                {"error": "No nearby subway station found."},
                status=404
            )

        serializer = self.get_serializer(nearest_station)
        return Response(serializer.data)
    




    @action(detail = False, methods=["get"])
    def within_radius(self, request):

        x = request.query_params.get("x")
        y= request.query_params.get("y")
        radius = request.query_params.get("radius")

        
        # Check that all parameters exist
        if not all([x, y, radius]):
            return Response(
                {"error": "x, y and radius are required."},
                status=400
            )
        
        try:
            x = float(x)
            y = float(y)
            radius = float(radius)
        except ValueError:
            return Response(
                {"error": "Coordinates and radius must be numeric values."},
                status=400
            )
        
        if radius <= 0:
            return Response(
            {"error": "Radius must be greater than zero."},
             status=400
        )
        
        # Create a point from the coordinates
        point = Point(x, y, srid=26918) 

        # Find subway stations within the specified radius
        stations_within_radius = (
            NycSubwayStation.objects
            .filter(
                geom__distance_lte=(point, radius)
            )
            .annotate(
                distance=Distance("geom", point)
            )
            .order_by("distance")
        )

        serializer = self.get_serializer(stations_within_radius, many=True)
        return Response(serializer.data)