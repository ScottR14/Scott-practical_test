from django.urls import path
from petsApp import views

app_name = 'pets'

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets, name='pets'),
]
