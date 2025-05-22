from django.shortcuts import render
from .models import Transaksi
from django.db.models import Sum
from datetime import date

def daftar_transaksi(request):
    transaksi = Transaksi.objects.all().order_by('-tanggal')
    return render(request, 'keuangan/daftar_transaksi.html', {'transaksi': transaksi})



def laporan_keuangan(request):
    semua_transaksi = Transaksi.objects.all().order_by('-tanggal')
    total_masuk = semua_transaksi.filter(jenis='masuk').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    total_keluar = semua_transaksi.filter(jenis='keluar').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    saldo = total_masuk - total_keluar

    return render(request, 'keuangan/laporan_keuangan.html', {
        'transaksi': semua_transaksi,
        'total_masuk': total_masuk,
        'total_keluar': total_keluar,
        'saldo': saldo,
    })