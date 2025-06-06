# Generated by Django 5.2.1 on 2025-05-15 12:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengumuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('isi', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('dibuat_oleh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopikDiskusi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('tanggal_buat', models.DateTimeField(auto_now_add=True)),
                ('pembuat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('penulis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentar', to='forum.topikdiskusi')),
            ],
        ),
    ]
