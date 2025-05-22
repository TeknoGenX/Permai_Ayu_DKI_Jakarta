from django.contrib import admin
from .models import AgendaKegiatan

@admin.register(AgendaKegiatan)
class AgendaKegiatanAdmin(admin.ModelAdmin):
    list_display = ('nama_kegiatan', 'tanggal_mulai', 'tanggal_selesai', 'lokasi', 'penanggung_jawab')
    list_filter = ('tanggal_mulai',)
    search_fields = ('nama_kegiatan', 'lokasi', 'penanggung_jawab')