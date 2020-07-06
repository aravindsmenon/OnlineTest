from rest_framework.fields import SerializerMethodField, FloatField
from rest_framework.serializers import ModelSerializer, Serializer


from TestApp.models import *


class UserSerializer(ModelSerializer):

    class Meta:
        model = files
        fields = '__all__'