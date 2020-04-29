from home.models import Data
import logging


def get_normalisasi():
    listdata = Data.objects.all()
    list_namaprodi = Data.objects.values_list('nama_prodi', flat=True)
    list_peminatprodi = Data.objects.values_list('peminat_prodi', flat=True)
    list_rerataipk = Data.objects.values_list('rerata_ipk', flat=True)
    list_kelulusan = Data.objects.values_list('kelulusan', flat=True)
    list_jamkehadirandosen = Data.objects.values_list('jam_kehadiran_dosen', flat=True)
    list_reratanilaidosen = Data.objects.values_list('rerata_nilai_dosen', flat=True)
    list_labelkelas = Data.objects.values_list('label_kelas', flat=True)

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

    n_data_normalisasi = []
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
        n_data_normalisasi.append(data)

    for i, x in enumerate(list_peminatprodi):
        n = (float(x) - minvalue['peminatprodi']) / (maxvalue['peminatprodi'] - minvalue['peminatprodi'])
        n_peminatprodi.append(n)
        n_data_normalisasi[i]['peminatprodi'] = float(n)

    for i, x in enumerate(list_rerataipk):
        n = (float(x) - minvalue['rerataipk']) / (maxvalue['rerataipk'] - minvalue['rerataipk'])
        n_rerataipk.append(n)
        n_data_normalisasi[i]['rerataipk'] = float(n)

    for i, x in enumerate(list_kelulusan):
        n = (float(x) - minvalue['kelulusan']) / (maxvalue['kelulusan'] - minvalue['kelulusan'])
        n_kelulusan.append(n)
        n_data_normalisasi[i]['kelulusan'] = float(n)

    for i, x in enumerate(list_jamkehadirandosen):
        n = (float(x) - minvalue['jamkehadirandosen']) / (maxvalue['jamkehadirandosen'] - minvalue['jamkehadirandosen'])
        n_jamkehadirandosen.append(n)
        n_data_normalisasi[i]['jamkehadirandosen'] = float(n)

    for i, x in enumerate(list_reratanilaidosen):
        n = (float(x) - minvalue['reratanilaidosen']) / (maxvalue['reratanilaidosen'] - minvalue['reratanilaidosen'])
        n_reratanilaidosen.append(n)
        n_data_normalisasi[i]['reratanilaidosen'] = float(n)

    # End Normalisasi

    data_normalisasi = {
        'n_data_normalisasi': n_data_normalisasi
    }

    return data_normalisasi
