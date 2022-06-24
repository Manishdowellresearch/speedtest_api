from django.urls import path
from .views import get_speed

urlpatterns = [
    path('get_speed', get_speed, name='get_speed'),
    ]