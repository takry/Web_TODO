from rest_framework.serializers import ModelSerializer

from todoapp.models import ToDo


class ToDoHyperlinkedModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'