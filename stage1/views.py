from django.shortcuts import render
from rest_framework import generics

from .models import zuriModel
from .serializers import ZuriSerializer


# Create your views here.
class backendTask(generics.ListAPIView):
    queryset = zuriModel.objects.all()
    serializer_class = ZuriSerializer