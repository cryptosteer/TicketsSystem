from rest_framework import serializers
from .models import Serie, Ticket


class SerieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serie
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    """docstring for TicketSerializer"""
    class Meta:
        model = Ticket
        fields = '__all__'
