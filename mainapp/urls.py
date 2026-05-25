from django.db import router
from django.urls import include, path
from rest_framework import routers
from mainapp.views import HabitsViewSet

router = routers.DefaultRouter()
router.register(r"Habits", HabitsViewSet, basename='habits')

urlpatterns = [
    path("", include(router.urls)),

]