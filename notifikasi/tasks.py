from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from agenda.models import AgendaKegiatan
from forum.models import Pengumuman
from django.contrib.auth.models import User

def kirim_reminder_agenda():
    besok = now().date() + timedelta(days=1)
    kegiatan_besok = AgendaKegiatan.objects.filter(tanggal_mulai=besok)

    if kegiatan_besok.exists():
        subject = "Reminder: Kegiatan Besok"
        message = "Berikut adalah kegiatan yang akan berlangsung besok:\n"
        for kegiatan in kegiatan_besok:
            message += f"- {kegiatan.nama_kegiatan} di {kegiatan.lokasi}\n"

        penerima = [user.email for user in User.objects.filter(is_active=True)]
        send_mail(subject, message, 'noreply@simo.com', penerima)

def kirim_notifikasi_pengumuman_terbaru():
    terbaru = Pengumuman.objects.order_by('-tanggal').first()
    if terbaru:
        subject = f"Pengumuman Baru: {terbaru.judul}"
        message = terbaru.isi
        penerima = [user.email for user in User.objects.filter(is_active=True)]
        send_mail(subject, message, 'noreply@simo.com', penerima)