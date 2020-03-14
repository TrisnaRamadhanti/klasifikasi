# Generated by Django 3.0.4 on 2020-03-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='akreditasi',
        ),
        migrations.RemoveField(
            model_name='data',
            name='id_jenj_didik',
        ),
        migrations.RemoveField(
            model_name='data',
            name='kelas',
        ),
        migrations.RemoveField(
            model_name='data',
            name='nama_lembaga',
        ),
        migrations.AddField(
            model_name='data',
            name='jam_kehadiran_dosen',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Rata-Rata Jam Kehadiran Dosen'),
        ),
        migrations.AddField(
            model_name='data',
            name='label_kelas',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Label Kelas Prodi'),
        ),
        migrations.AddField(
            model_name='data',
            name='nama_prodi',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nama Program Studi'),
        ),
        migrations.AddField(
            model_name='data',
            name='rerata_nilai_dosen',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Rata-Rata Nilai Dosen'),
        ),
        migrations.AddField(
            model_name='data',
            name='tahun_smstr',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tahun Semester'),
        ),
        migrations.AlterField(
            model_name='data',
            name='kelulusan',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Jumlah Lulusan Mahasiswa'),
        ),
        migrations.AlterField(
            model_name='data',
            name='peminat_prodi',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Presentase % Peminat Prodi'),
        ),
    ]
