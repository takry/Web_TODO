from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from authapp.models import UserAuth, Project
from authapp.serialiazers import UserAuthModelSerializer, ProjectHyperlinkedModelSerializer


# Create your views here.
class UserAuthModelViewSet(ModelViewSet):
    queryset = UserAuth.objects.all()
    serializer_class = UserAuthModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer
