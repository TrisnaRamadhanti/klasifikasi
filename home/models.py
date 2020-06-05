from django.db import models


class Data(models.Model):
    semester_mulai = models.CharField("Semester Mulai", max_length=10, blank=True, null=True, )
    kode_prodi = models.CharField("Kode Prodi", max_length=20, blank=True, null=True)
    tahun_smstr = models.CharField("Tahun Semester", max_length=20, blank=True, null=True)
    nama_prodi = models.CharField("Nama Program Studi", max_length=255, blank=True, null=True)
    peminat_prodi = models.CharField("Presentase % Peminat Prodi", max_length=50, blank=True, null=True)
    rerata_ipk = models.CharField("Rerata IPK", max_length=50, blank=True, null=True)
    kelulusan = models.CharField("Jumlah Lulusan Mahasiswa", max_length=50, blank=True, null=True)
    jam_kehadiran_dosen = models.CharField("Rata-Rata Jam Kehadiran Dosen", max_length=50, blank=True, null=True)
    rerata_nilai_dosen = models.CharField("Rata-Rata Nilai Dosen", max_length=50, blank=True, null=True)
    label_kelas = models.CharField("Label Kelas Prodi", max_length=30, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.kode_prodi


class TrainingSvmSeq(models.Model):
    id = models.IntegerField('id', primary_key=True)
    lamda = models.CharField('Lambda', max_length=100, blank=True, null=True)
    sigma = models.CharField('Sigma', max_length=100, blank=True, null=True)
    constant = models.CharField('Constant', max_length=100, blank=True, null=True)
    gamma = models.CharField('Gamma', max_length=100, blank=True, null=True)
    iterasi = models.CharField('Iterasi', max_length=100, blank=True, null=True)
    k_fold = models.CharField('KFold (Split)', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id


class TrainingSvmSmo(models.Model):
    id = models.IntegerField('id', primary_key=True)
    constant = models.CharField('Constant', max_length=100, blank=True, null=True)
    iterasi = models.CharField('Iterasi', max_length=100, blank=True, null=True)
    k_fold = models.CharField('KFold (Split)', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id


class TrainingNaiveBayes(models.Model):
    id = models.IntegerField('id', primary_key=True)
    k_fold = models.CharField('KFold (Split)', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id
