from django.contrib import admin
from .models import DokumentasiKegiatan

@admin.register(DokumentasiKegiatan)
class DokumentasiKegiatanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')
    search_fields = ('judul', 'deskripsi')
    list_filter = ('tanggal',)