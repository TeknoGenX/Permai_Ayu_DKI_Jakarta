from django.shortcuts import render
from .models import Anggota

def daftar_anggota(request):
    anggota = Anggota.objects.all().order_by('nama')
    return render(request, 'anggota/daftar_anggota.html', {'anggota': anggota})