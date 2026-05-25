from rest_framework import serializers
from .models import Habits
from django.contrib.auth.models import User
from rest_framework import serializers

class HabitsSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    class Meta:
        model = Habits
        fields = ['id', 'name', 'cost', 'frequency', 'period', "total_cost", 'total_days']
    def get_total_cost(self, obj):
        return obj.total_cost()
    def get_total_days(self, obj):
        return obj.total_days()