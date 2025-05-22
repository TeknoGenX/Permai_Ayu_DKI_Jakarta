from django.shortcuts import render
from .models import TopikDiskusi, Komentar, Pengumuman

def daftar_topik(request):
    topik = TopikDiskusi.objects.all().order_by('-tanggal_buat')
    return render(request, 'forum/daftar_topik.html', {'topik': topik})

def daftar_pengumuman(request):
    pengumuman = Pengumuman.objects.all().order_by('-tanggal')
    return render(request, 'forum/daftar_pengumuman.html', {'pengumuman': pengumuman})