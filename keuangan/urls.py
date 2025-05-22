from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_transaksi, name='daftar_transaksi'),
    path('', views.laporan_keuangan, name='laporan_keuangan'),
]