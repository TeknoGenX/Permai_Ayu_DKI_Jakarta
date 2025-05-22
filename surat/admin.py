from django.contrib import admin
from .models import Surat

@admin.register(Surat)
class SuratAdmin(admin.ModelAdmin):
    list_display = ('nomor_surat', 'jenis', 'tanggal', 'pengirim_penerima', 'perihal')
    list_filter = ('jenis', 'tanggal')
    search_fields = ('nomor_surat', 'perihal', 'pengirim_penerima')