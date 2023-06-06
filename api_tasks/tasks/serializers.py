from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.serializers import UserSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
