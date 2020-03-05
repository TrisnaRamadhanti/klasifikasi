# Generated by Django 3.0.3 on 2020-02-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_mulai', models.CharField(blank=True, max_length=10, null=True, verbose_name='Semester Mulai')),
                ('kode_prodi', models.CharField(blank=True, max_length=20, null=True, verbose_name='Kode Prodi')),
                ('tahun_smstr', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tahun Semester')),
                ('nama_prodi', models.CharField(blank=True, max_length=10, null=True, verbose_name='Nama Prodi')),
                ('peminat_prodi', models.CharField(blank=True, max_length=20, null=True, verbose_name='Peminat Prodi')),
                ('rerata_ipk', models.CharField(blank=True, max_length=10, null=True, verbose_name='Rerata IPK')),
                ('kelulusan', models.CharField(blank=True, max_length=10, null=True, verbose_name='Kelulusan')),
                ('jam_kehadiran_dosen', models.CharField(blank=True, max_length=10, null=True, verbose_name='Jam Kehadiran Dosen')),
                ('rerata_nilai_dosen', models.CharField(blank=True, max_length=10, null=True, verbose_name='Rata-Rata Nilai Dosen')),
                ('label_kelas', models.CharField(blank=True, max_length=30, null=True, verbose_name='Label Kelas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
    ]
