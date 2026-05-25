from django.shortcuts import render
from rest_framework import viewsets
from .models import Habits
from .serializers import HabitsSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

class Habits_Filter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    cost = django_filters.NumberFilter()
    cost_min = django_filters.NumberFilter(field_name='cost', lookup_expr='gte')
    cost_max = django_filters.NumberFilter(field_name='cost', lookup_expr='lte')
    frequency = django_filters.NumberFilter()
    period = django_filters.CharFilter(lookup_expr='exact')
    
    class Meta:
        model = Habits
        fields = ['name', 'cost', 'frequency', 'period']

class Our_throttle(AnonRateThrottle):
    scope = "example"

class Our_pagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    max_page_size = 10000

class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = Our_pagination
    throttle_classes = [Our_throttle,]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Habits_Filter
