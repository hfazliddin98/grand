from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from grand_ariza.models import Ariza
from grand_api.serializers import ArizaGetSerializer, ArizaPostSerializer




class ArizaViewSet(ModelViewSet):
    queryset = Ariza.objects.all()
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return ArizaGetSerializer
        return ArizaPostSerializer  # POST, PUT, PATCH uchun