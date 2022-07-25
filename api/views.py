from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from api.models import Room
from .serializers import RoomSerializer


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer





