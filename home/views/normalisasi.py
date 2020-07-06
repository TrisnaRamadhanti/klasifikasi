import numpy as np
from home.models import Data


def get_normalisasi(tahun=None):

    if tahun is None:
        listdata = Data.objects.all()
        list_peminatprodi = Data.objects.values_list('peminat_prodi', flat=True)
        list_rerataipk = Data.objects.values_list('rerata_ipk', flat=True)
        list_kelulusan = Data.objects.values_list('kelulusan', flat=True)
        list_jamkehadirandosen = Data.objects.values_list('jam_kehadiran_dosen', flat=True)
        list_reratanilaidosen = Data.objects.values_list('rerata_nilai_dosen', flat=True)
    else:
        listdata = Data.objects.filter(tahun_smstr=tahun)
        list_peminatprodi = listdata.values_list('peminat_prodi', flat=True)
        list_rerataipk = listdata.values_list('rerata_ipk', flat=True)
        list_kelulusan = listdata.values_list('kelulusan', flat=True)
        list_jamkehadirandosen = listdata.values_list('jam_kehadiran_dosen', flat=True)
        list_reratanilaidosen = listdata.values_list('rerata_nilai_dosen', flat=True)

    minvalue = {
        'peminatprodi': min([float(i) for i in list_peminatprodi]),
        'rerataipk': min([float(i) for i in list_rerataipk]),
        'kelulusan': min([float(i) for i in list_kelulusan]),
        'jamkehadirandosen': min([float(i) for i in list_jamkehadirandosen]),
        'reratanilaidosen': min([float(i) for i in list_reratanilaidosen])
    }

    maxvalue = {
        'peminatprodi': max([float(i) for i in list_peminatprodi]),
        'rerataipk': max([float(i) for i in list_rerataipk]),
        'kelulusan': max([float(i) for i in list_kelulusan]),
        'jamkehadirandosen': max([float(i) for i in list_jamkehadirandosen]),
        'reratanilaidosen': max([float(i) for i in list_reratanilaidosen])
    }

    data_normalisasi_view = []
    data_normalisasi = []

    n_peminatprodi = []
    n_rerataipk = []
    n_kelulusan = []
    n_jamkehadirandosen = []
    n_reratanilaidosen = []

    # Normalisasi

    for x in listdata:
        if x.label_kelas == 'Berkembang':
            label = '1'
        else:
            label = '-1'

        data = {
            'namaprodi': x.nama_prodi,
            'peminatprodi': 0,
            'rerataipk': 0,
            'kelulusan': 0,
            'jamkehadirandosen': 0,
            'reratanilaidosen': 0,
            'label': label
        }
        data_normalisasi_view.append(data)

    for i, x in enumerate(list_peminatprodi):
        minmax = maxvalue['peminatprodi'] - minvalue['peminatprodi']
        if minmax > 0:
            n = (float(x) - minvalue['peminatprodi']) / minmax
            n_peminatprodi.append(n)
            data_normalisasi_view[i]['peminatprodi'] = float(n)
            data_normalisasi.append([float(n), 0, 0, 0, 0])
        else:
            data_normalisasi.append([0, 0, 0, 0, 0])

    for i, x in enumerate(list_rerataipk):
        minmax = maxvalue['rerataipk'] - minvalue['rerataipk']
        if minmax > 0:
            n = (float(x) - minvalue['rerataipk']) / minmax
            n_rerataipk.append(n)
            data_normalisasi_view[i]['rerataipk'] = float(n)
            data_normalisasi[i][1] = float(n)

    for i, x in enumerate(list_kelulusan):
        minmax = maxvalue['kelulusan'] - minvalue['kelulusan']
        if minmax > 0:
            n = (float(x) - minvalue['kelulusan']) / minmax
            n_kelulusan.append(n)
            data_normalisasi_view[i]['kelulusan'] = float(n)
            data_normalisasi[i][2] = float(n)

    for i, x in enumerate(list_jamkehadirandosen):
        minmax = maxvalue['jamkehadirandosen'] - minvalue['jamkehadirandosen']
        if minmax > 0:
            n = (float(x) - minvalue['jamkehadirandosen']) / minmax
            n_jamkehadirandosen.append(n)
            data_normalisasi_view[i]['jamkehadirandosen'] = float(n)
            data_normalisasi[i][3] = float(n)

    for i, x in enumerate(list_reratanilaidosen):
        minmax = maxvalue['reratanilaidosen'] - minvalue['reratanilaidosen']
        if minmax > 0:
            n = (float(x) - minvalue['reratanilaidosen']) / minmax
            n_reratanilaidosen.append(n)
            data_normalisasi_view[i]['reratanilaidosen'] = float(n)
            data_normalisasi[i][4] = float(n)

    # End Normalisasi

    normalisasi = {
        'data_normalisasi_view': data_normalisasi_view,
        'data_normalisasi': np.asarray(data_normalisasi)
    }

    return normalisasi
