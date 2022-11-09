from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from authapp.models import UserAuth, Project
from authapp.serialiazers import UserAuthModelSerializer, ProjectHyperlinkedModelSerializer, UserAuthModelSerializerFull
from filters import ProjectFilter


# Create your views here.
class UserAuthCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserAuth.objects.all()
    serializer_class = UserAuthModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserAuthModelSerializerFull
        return UserAuthModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPaginationViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer
    # pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter
