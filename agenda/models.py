from django.db import models

class AgendaKegiatan(models.Model):
    nama_kegiatan = models.CharField(max_length=200)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    lokasi = models.CharField(max_length=200)
    penanggung_jawab = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nama_kegiatan} ({self.tanggal_mulai} - {self.tanggal_selesai})"