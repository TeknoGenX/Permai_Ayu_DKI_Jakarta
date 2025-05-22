from django.contrib import admin
from .models import TopikDiskusi, Komentar, Pengumuman

admin.site.register(TopikDiskusi)
admin.site.register(Komentar)
admin.site.register(Pengumuman)