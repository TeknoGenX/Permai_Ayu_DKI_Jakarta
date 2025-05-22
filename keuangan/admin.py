from django.contrib import admin
from .models import Transaksi

@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('tanggal', 'tipe', 'jumlah', 'keterangan', 'jenis')
    list_filter = ('tipe', 'tanggal', 'jenis')
    search_fields = ('keterangan',)
