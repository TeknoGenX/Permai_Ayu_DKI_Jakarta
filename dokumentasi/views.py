from django.shortcuts import render
from .models import DokumentasiKegiatan

def daftar_dokumentasi(request):
    dokumentasi = DokumentasiKegiatan.objects.all().order_by('-tanggal')
    return render(request, 'dokumentasi/daftar_dokumentasi.html', {'dokumentasi': dokumentasi})