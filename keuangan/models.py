from django.db import models

# Create your models here.

class Transaksi(models.Model):
    TIPE_TRANSAKSI = [
        ('masuk', 'Kas Masuk'),
        ('keluar', 'Pengeluaran'),
        ('denda', 'Denda'),
    ]

    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.TextField()
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    tipe = models.CharField(max_length=10, choices=TIPE_TRANSAKSI)

    def __str__(self):
        return f"{self.get_tipe_display()} - {self.jumlah} ({self.tanggal})"
    
    JENIS_TRANSAKSI = [
        ('masuk', 'Pemasukan'),
        ('keluar', 'Pengeluaran'),
    ]

    tanggal = models.DateField()
    jenis = models.CharField(max_length=10, choices=JENIS_TRANSAKSI)
    keterangan = models.CharField(max_length=200)
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.get_jenis_display()} - {self.keterangan} - Rp{self.jumlah}"
