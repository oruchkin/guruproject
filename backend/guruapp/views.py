import datetime
from itertools import chain
from rest_framework import status
from django.db.models import (F, Q)
from django.http import  HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .utils import (get_object)
from .models import (Shop, City, Street)
from .serializer import (City_serializer,Street_serializer,Shop_serializer)

def index(request):
    """ Главная страница """
    return HttpResponse("это главная страница для тестового задания Гуру Групп")


class City_list(APIView):
    """ API для вывода ВСЕХ городов """
    permission_classes = [AllowAny]
    def get(self, request): 
        serializer = City_serializer(City.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class City_detail(APIView):
    """ API для вывода конкретного города"""
    def get(self, request, pk, format=None):
        object = get_object(City,pk)
        if not object:
            return Response({"error":"город не найден"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = City_serializer(object)
        return Response(serializer.data)


class City_street(APIView):
    """ API для вывода всех улиц города"""
    def get(self, request, pk, format=None):
        city = get_object(City,pk)
        if not city:
            return Response({"error":"город не найден"}, status=status.HTTP_400_BAD_REQUEST)
        all_streats = Street.objects.filter(city=city)
        serializer = Street_serializer(all_streats, many=True)
        return Response(serializer.data)


class New_shop(APIView):
    """ API для создания магазина и просмотра с фильтрами магазинов """
    def get(self, request): 
        city = request.query_params.get('city')
        open = request.query_params.get('open')
        street = request.query_params.get('street')
        time = request.query_params.get('time')
        if city:
            city = get_object(City,city)
            if not city:
                return Response({"error":"город не найден"}, status=status.HTTP_400_BAD_REQUEST)
            
        if street:
            street = get_object(Street,street)
            if not street:
                return Response({"error":"улица не найдена"}, status=status.HTTP_400_BAD_REQUEST)

        now = datetime.datetime.now()
        if time:
            t=time.split(":")
            now = datetime.time(hour=int(t[0]), minute=int(t[1]))
        time_now = f"{now.hour}:{now.minute}:{now.second}"

        #фильтры:
        if city and street and open == "1":
            queryset = Shop.objects.filter(Q(Q(Q(time_open__gt=F('time_closed')), Q(time_closed__gt=time_now),Q(time_open__gt=time_now),Q(city=city), Q(street=street))| 
                                            Q(Q(time_open__gt=F('time_closed')), Q(time_open__lt=time_now),Q(city=city), Q(street=street)))|
                                            Q(Q(time_open__lt=time_now, time_closed__gt=time_now, city=city, street=street)))

        elif city and open == "1":            
            queryset = Shop.objects.filter(Q(Q(Q(time_open__gt=F('time_closed')), Q(time_closed__gt=time_now),Q(time_open__gt=time_now),Q(city=city))| 
                                            Q(Q(time_open__gt=F('time_closed')), Q(time_open__lt=time_now),Q(city=city)))|
                                            Q(Q(time_open__lt=time_now, time_closed__gt=time_now, city=city)))
            
        elif street and open == "1":
            queryset = Shop.objects.filter(Q(Q(Q(time_open__gt=F('time_closed')), Q(time_closed__gt=time_now),Q(time_open__gt=time_now),Q(street=street))| 
                                            Q(Q(time_open__gt=F('time_closed')), Q(time_open__lt=time_now),Q(street=street)))|
                                            Q(Q(time_open__lt=time_now, time_closed__gt=time_now, street=street)))

        if city and street and open == "0":
            queryset = Shop.objects.filter((Q(Q(time_open__gt=F('time_closed')), Q(time_closed__lt=time_now),Q(time_open__gt=time_now), Q(city=city), Q(street=street)))|
                                            Q(Q(time_open__lt=F('time_closed')), 
                                            Q(Q(time_open__gt=time_now) , Q(time_closed__gt=time_now))| 
                                            Q(Q(time_open__lt=time_now) , Q(time_closed__lt=time_now),Q(city=city), Q(street=street))))

        elif city and open == "0":
            queryset = Shop.objects.filter((Q(Q(time_open__gt=F('time_closed')), Q(time_closed__lt=time_now),Q(time_open__gt=time_now), Q(city=city)))|
                                            Q(Q(time_open__lt=F('time_closed')), 
                                            Q(Q(time_open__gt=time_now) , Q(time_closed__gt=time_now))| 
                                            Q(Q(time_open__lt=time_now) , Q(time_closed__lt=time_now),Q(city=city))))

        elif street and open == "0":            
            queryset = Shop.objects.filter((Q(Q(time_open__gt=F('time_closed')), Q(time_closed__lt=time_now),Q(time_open__gt=time_now), Q(street=street)))|
                                            Q(Q(time_open__lt=F('time_closed')), 
                                            Q(Q(time_open__gt=time_now) , Q(time_closed__gt=time_now))| 
                                            Q(Q(time_open__lt=time_now) , Q(time_closed__lt=time_now),Q(street=street))))

        elif city and street:
            queryset = Shop.objects.filter(city=city, street=street)
            
        elif city:
            queryset = Shop.objects.filter(city=city)

        elif street:
            queryset = Shop.objects.filter(street=street)

        elif open == "1":
            queryset = Shop.objects.filter(Q(Q(Q(time_open__gt=F('time_closed')), Q(time_closed__gt=time_now),Q(time_open__gt=time_now))| 
                                            Q(Q(time_open__gt=F('time_closed')), Q(time_open__lt=time_now)))|
                                            Q(Q(time_open__lt=time_now, time_closed__gt=time_now)))

        elif open == "0":            
            queryset = Shop.objects.filter((Q(Q(time_open__gt=F('time_closed')), Q(time_closed__lt=time_now),Q(time_open__gt=time_now)))|
                                            Q(Q(time_open__lt=F('time_closed')), 
                                            Q(Q(time_open__gt=time_now) , Q(time_closed__gt=time_now))| 
                                            Q(Q(time_open__lt=time_now) , Q(time_closed__lt=time_now))))

        else:
            queryset = Shop.objects.all()
        serializer = Shop_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = Shop_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


