from django.shortcuts import render
from .models import AgendaKegiatan
from datetime import date

def daftar_agenda(request):
    hari_ini = date.today()
    kegiatan_terdekat = AgendaKegiatan.objects.filter(tanggal_selesai__gte=hari_ini).order_by('tanggal_mulai')
    return render(request, 'agenda/daftar_agenda.html', {'agenda': kegiatan_terdekat})