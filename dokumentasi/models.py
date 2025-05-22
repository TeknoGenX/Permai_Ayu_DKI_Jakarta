from django.db import models

class DokumentasiKegiatan(models.Model):
    judul = models.CharField(max_length=200)
    tanggal = models.DateField()
    deskripsi = models.TextField(blank=True)
    file_foto = models.ImageField(upload_to='dokumentasi/foto/', blank=True, null=True)
    file_video = models.FileField(upload_to='dokumentasi/video/', blank=True, null=True)

    def __str__(self):
        return f"{self.judul} ({self.tanggal})"