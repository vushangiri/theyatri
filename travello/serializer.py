from django.db import models
from rest_framework import serializers
from .models import Destination,subscribe

class DestinationSerial(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['name','img','desc','price','offer','sittayma','vid']

class subscribeSerial(serializers.ModelSerializer):
    class Meta:
        model = subscribe
        fields = ['name','email']
