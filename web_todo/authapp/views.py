from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from authapp.models import UserAuth
from authapp.serialiazers import UserAuthModelSerializer


# Create your views here.
class UserAuthModelViewSet(ModelViewSet):
    queryset = UserAuth.objects.all()
    serializer_class = UserAuthModelSerializer
