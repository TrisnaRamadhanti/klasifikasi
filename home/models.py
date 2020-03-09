from django.db import models


class Data(models.Model):
    semester_mulai = models.CharField("Semester Mulai", max_length=10, blank=True, null=True)
    kode_prodi = models.CharField("Kode Prodi", max_length=20, blank=True, null=True)
    nama_lembaga = models.CharField("Nama Lembaga", max_length=255, blank=True, null=True)
    id_jenj_didik = models.CharField("Id Didik", max_length=10, blank=True, null=True)
    peminat_prodi = models.CharField("Peminat Prodi", max_length=20, blank=True, null=True)
    rerata_ipk = models.CharField("Rerata IPK", max_length=10, blank=True, null=True)
    kelulusan = models.CharField("Kelulusan", max_length=10, blank=True, null=True)
    akreditasi = models.CharField("Akreditasi", max_length=10, blank=True, null=True)
    kelas = models.CharField("Kelas", max_length=30, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.kode_prodi
