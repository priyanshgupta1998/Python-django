from .serializers import serializers
from .models import Stock
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Lists all stocks or create a new one
#stcoks/
class StockList(APIView):
    def get(self , request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks , many = True)
        return Response(serializer.data)
    
    def post(self):
        pass