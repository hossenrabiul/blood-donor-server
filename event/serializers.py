from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event


class CreatedByEvent(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class EventSerializer(serializers.ModelSerializer):
    user = CreatedByEvent(many=False,read_only=True)
    class Meta:
        model = Event
        fields = "__all__"
