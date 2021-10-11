from django.shortcuts import render

from credits.models import Solicitude, Client
from credits.serializer import ClientSerializer, SolicitudeSerializer
from rest_framework import viewsets


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    search_fields = ['dni', 'name', 'punctuation','debt_sbs']
    ordering = ['id']
    filterset_fields = {'dni': ['exact', 'gte', 'lte','gt', 'lt'],
                        'name': ['exact', 'gte', 'lte', 'gt', 'lt'],
                        'punctuation': ['exact', 'gte', 'lte', 'gt', 'lt'],
                        'debt_sbs': ['exact', 'gte', 'lte', 'gt', 'lt'],
    }
                        
class SolicitudeViewSet(viewsets.ModelViewSet):
    queryset = Solicitude.objects.all()
    serializer_class = SolicitudeSerializer
    search_fields = ['state','credit_indicator','client']
    ordering = ['id']
    filterset_fields = {'state': ['exact', 'gte', 'lte','gt', 'lt'],
                        'credit_indicator': ['exact', 'gte', 'lte', 'gt', 'lt'],
    }