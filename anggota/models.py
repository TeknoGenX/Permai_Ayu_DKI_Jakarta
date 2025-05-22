from django.db import models

class Anggota(models.Model):
    STATUS_ANGGOTA = [
        ('aktif', 'Aktif'),
        ('alumni', 'Alumni'),
    ]

    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    no_hp = models.CharField(max_length=15)
    alamat = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_ANGGOTA, default='aktif')
    tanggal_gabung = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} ({self.get_status_display()})"