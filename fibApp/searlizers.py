from rest_framework import serializers
from .models import fibonacci

class fibSerailizers (serializers.ModelSerializer):
    class Meta:
        model = fibonacci
        fields = ('id', 'number', 'time')

