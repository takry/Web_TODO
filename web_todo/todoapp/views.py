from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todoapp.models import ToDo
from todoapp.serialiazers import ToDoHyperlinkedModelSerializer


# Create your views here.
class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoHyperlinkedModelSerializer