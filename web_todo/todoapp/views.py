
from rest_framework import status
from rest_framework.mixins import DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todoapp.models import ToDo
from todoapp.serialiazers import ToDoHyperlinkedModelSerializer


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class DestroyModelMixin(DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class ToDoLimitOffsetPaginationViewSet(DestroyModelMixin, ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoHyperlinkedModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_fields = ['project']
