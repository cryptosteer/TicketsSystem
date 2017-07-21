from rest_framework import serializers
from .models import Ticket, TicketPriority, TicketProblem


class TicketSerializer(serializers.ModelSerializer):
    """docstring for TicketSerializer"""
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketPrioritySerializer(serializers.ModelSerializer):
    """docstring for TicketPrioritySerializer"""
    class Meta:
        model = TicketPriority
        fields = '__all__'


class TicketProblemSerializer(serializers.ModelSerializer):
    """docstring for TicketProblemSerializer"""
    class Meta:
        model = TicketProblem
        fields = '__all__'


class TicketListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order = serializers.CharField(required=False, allow_blank=True, max_length=100)
    created = serializers.CharField(required=False, allow_blank=True, max_length=100)
    priority = serializers.CharField(required=False, allow_blank=True, max_length=100)
    problem = serializers.CharField(required=False, allow_blank=True, max_length=100)
    status = serializers.CharField(required=False, allow_blank=True, max_length=100)
    agent = serializers.CharField(required=False, allow_blank=True, max_length=100)


class TicketItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order = serializers.CharField(required=False, allow_blank=True, max_length=100)
    created = serializers.CharField(required=False, allow_blank=True, max_length=100)
    closed = serializers.CharField(required=False, allow_blank=True, max_length=100)
    created_by = serializers.CharField(required=False, allow_blank=True, max_length=100)
    priority = serializers.CharField(required=False, allow_blank=True, max_length=100)
    problem = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True, max_length=100)
    agent = serializers.CharField(required=False, allow_blank=True, max_length=100)
