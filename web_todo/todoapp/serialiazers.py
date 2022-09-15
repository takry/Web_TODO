from rest_framework.serializers import HyperlinkedModelSerializer

from todoapp.models import ToDo


class ToDoHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'