from rest_framework.serializers import ModelSerializer

from .models import UserAuth


class UserAuthModelSerializer(ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ('username', 'first_name', 'last_name', 'email',)
