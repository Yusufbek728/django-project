from django.contrib import admin
from .models import Habits

@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost', 'frequency', 'period', 'total_cost']
    search_fields = ['name']
    list_filter = ['period']
