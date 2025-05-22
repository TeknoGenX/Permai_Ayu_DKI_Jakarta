from django.db import models

class Surat(models.Model):
    JENIS_SURAT = [
        ('masuk', 'Surat Masuk'),
        ('keluar', 'Surat Keluar'),
    ]

    jenis = models.CharField(max_length=10, choices=JENIS_SURAT)
    nomor_surat = models.CharField(max_length=50, unique=True)
    tanggal = models.DateField()
    pengirim_penerima = models.CharField(max_length=100)
    perihal = models.CharField(max_length=200)
    file_surat = models.FileField(upload_to='surat/')
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_jenis_display()} - {self.nomor_surat}"