from django.db import models
from django.contrib.auth.models import User

class TopikDiskusi(models.Model):
    judul = models.CharField(max_length=200)
    pembuat = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_buat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

class Komentar(models.Model):
    topik = models.ForeignKey(TopikDiskusi, on_delete=models.CASCADE, related_name='komentar')
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Komentar oleh {self.penulis.username} pada {self.topik.judul}"

class Pengumuman(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    dibuat_oleh = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.judul