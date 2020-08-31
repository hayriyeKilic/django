from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name="vehicle_list"),
]
