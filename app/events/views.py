from datetime import datetime
from urllib.parse import unquote
import traceback
import sys
# Django
from django.db.models import Q
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
# REST Framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
# LOCAL Pies
from .models import Event, EventType
from .serializers import EventSerializer, EventTypeSerializer
 

class GetEventType(APIView):

    def get(self, request, name=''):

        try:
            events = Event.objects.filter(eventType__name__icontains=name)
            serializer = EventSerializer(events, many=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except: 
            exc_info = sys.exc_info()
            return Response(traceback.format_exception(*exc_info), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class GetEvent(APIView):

    optional_params = ['name','date','eventType']

    def get(self, request, *args, **kwargs):

        try: 
            #Filter params in case the user entered extra ones
            op = dict((key,value) for key, value in request.GET.items() if key in optional_params)

            lat = kwargs['lat']
            lon = kwargs['lon']
            rad = int(kwargs['rad'])
            count = int(kwargs['count'])

            #Compile Q Model 
            and_condition = Q()
            for key, value in op.items():
                if 'name' == key:
                    and_condition.add(Q(**{key+'__icontains': value}), Q.AND)
                else:
                    and_condition.add(Q(**{key: value}), Q.AND)

            #Create the GEOS point based on lat and lon
            point = GEOSGeometry('POINT({lat} {lon})'.format(lat=lat, lon=lon), srid=4326)

            #Query the database using the GEOS point/ Radius / 
            qs = Event.objects.filter(location__distance_lte=(point, rad))
            qs = qs.filter(and_condition)[:count]
            serializer = EventSerializer(qs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            exc_info = sys.exc_info()
            return Response(traceback.format_exception(*exc_info), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
