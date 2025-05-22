from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_surat, name='daftar_surat'),
]