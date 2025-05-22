from django.contrib import admin
from .models import Anggota

@admin.register(Anggota)
class AnggotaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'no_hp', 'status', 'tanggal_gabung')
    list_filter = ('status', 'tanggal_gabung')
    search_fields = ('nama', 'email', 'no_hp')