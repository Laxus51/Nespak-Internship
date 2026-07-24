from django.db import connection

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers import TopNeighborhoodSerializer


class DashboardViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["get"])
    def top_neighborhoods(self, request):

        sql = """
        SELECT
            n.name,
            COUNT(s.id) AS station_count
        FROM
            nyc_neighborhoods n
        LEFT JOIN
            nyc_subway_stations s
            ON ST_Contains(n.geom, s.geom)
        GROUP BY
            n.id,
            n.name
        ORDER BY
            station_count DESC,
            n.name ASC
        LIMIT 10;
        """

        with connection.cursor() as cursor:
            cursor.execute(sql)

            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()

        results = [
            dict(zip(columns, row))
            for row in rows
        ]

        serializer = TopNeighborhoodSerializer(results, many=True)

        return Response(serializer.data)