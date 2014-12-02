from .models import Biker
from .serializers import Bikerserializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from datetime import datetime

class BikerList(APIView):
	
	def get(self,request,format=None):
		bikers=Biker.objects.all()
		serialized_biker=Bikerserializer(bikers,many=True)
		return Response(serialized_biker.data)


class BikerSetInfo(APIView):
	def post(self,request,format=None):
		if request.method == 'POST':
			bikerId = int(request.DATA['id'])
			start = datetime.strptime(str(request.DATA['start']), '%H:%M:%S')
			stage1 = datetime.strptime(str(request.DATA['first']), '%H:%M:%S')
			stage2 = datetime.strptime(str(request.DATA['second']), '%H:%M:%S')
			last = datetime.strptime(str(request.DATA['last']), '%H:%M:%S')
			Biker.objects.filter(pk=bikerId).update(
				start_time=start,
				first_check=stage1,
				second_check=stage2,
				final_check=last
			)
			print "All ok!"
			return Response({'Status':'Success!','Received Data': request.DATA})
		return Response("Some Error was occured")