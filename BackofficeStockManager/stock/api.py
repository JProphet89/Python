from .models import Stock
from .serializers import Stockserializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

class StockList(APIView):
	
	def get(self,request,format=None):
		stocks=Stock.objects.all()
		serialized_stock=Stockserializer(stocks,many=True)
		return Response(serialized_stock.data)