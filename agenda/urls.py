from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_agenda, name='daftar_agenda'),
]