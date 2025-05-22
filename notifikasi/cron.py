from django_cron import CronJobBase, Schedule
from .tasks import kirim_reminder_agenda, kirim_notifikasi_pengumuman_terbaru

class ReminderAgendaJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24  # Setiap hari

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'notifikasi.reminder_agenda'

    def do(self):
        kirim_reminder_agenda()

class NotifikasiPengumumanJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 6  # Setiap 6 jam

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'notifikasi.pengumuman'

    def do(self):
        kirim_notifikasi_pengumuman_terbaru()