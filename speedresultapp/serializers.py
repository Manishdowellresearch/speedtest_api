from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Speed_test_data


class SpeedSerializer(ModelSerializer):
    class Meta:
        model = Speed_test_data
        fields = '__all__'


