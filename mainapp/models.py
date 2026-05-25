from django.db import models
from datetime import datetime, timedelta, time, date
choices = (
    ('oy', 'month'),
    ('hafta', 'week'),
    ('yil', 'year'),
    ('total', 'total')
)
bugun = date.today()
class Habits(models.Model):
    name = models.CharField(max_length=50, verbose_name= 'habits name')
    cost = models.PositiveIntegerField(verbose_name= 'cost')
    frequency = models.PositiveIntegerField(default=1, verbose_name='bir kunda qancha olasiz')
    period = models.CharField(choices=choices, verbose_name='period')
    since = models.DateField(default=bugun, verbose_name='nechta kun oldin boshlangan')
    def __str__(self):
        return self.name    
    def total_cost(self):
        if self.period == 'oy':
         return self.cost * self.frequency * 30

        elif self.period == 'hafta':
            return self.cost * self.frequency * 7

        elif self.period == 'yil':
            return self.cost * self.frequency * 365

        elif self.period == 'total':
            return self.cost * self.frequency * self.total_days()

    def total_days(self):
        total_days = bugun - self.since
        return total_days.days
        