from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import UserAuth, Project


class UserAuthModelSerializer(ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ('username', 'first_name', 'last_name', 'email',)


class UserAuthModelSerializerFull(ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ('username', 'first_name', 'last_name', 'email','is_superuser', 'is_staff')


class ProjectHyperlinkedModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
