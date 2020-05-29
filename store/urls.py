from django.contrib import admin
from django.urls import path
from .views import index , signup

urlpatterns = [
   path('', index),
   path('signup' , signup)
]
