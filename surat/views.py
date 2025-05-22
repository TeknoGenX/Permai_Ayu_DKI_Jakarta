from django.shortcuts import render
from .models import Surat

def daftar_surat(request):
    surat = Surat.objects.all().order_by('-tanggal')
    return render(request, 'surat/daftar_surat.html', {'surat': surat})