"""
    This is the views for the api_demo
"""
from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from apidemo.serializers import GameRecordSerializer
from apidemo import models


class GameRecordView(APIView):

    def get(self, request):
        record = models.GameRecord.objects.all()
        seri = GameRecordSerializer(record, many=True)
        return Response(seri.data)

    def post(self, request):
        sid = transaction.savepoint()
        serializer = GameRecordSerializer(models.GameRecord, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # transaction.savepoint_rollback(sid)
            return Response(serializer.data)
        else:
            return Response("Error!")

