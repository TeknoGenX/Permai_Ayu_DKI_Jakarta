from django.urls import path
from . import views

urlpatterns = [
    path('diskusi/', views.daftar_topik, name='daftar_topik'),
    path('pengumuman/', views.daftar_pengumuman, name='daftar_pengumuman'),
]