from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_dokumentasi, name='daftar_dokumentasi'),
]