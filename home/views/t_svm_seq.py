import math
from home.views import normalisasi


def get_kernel():

    n_data_normalisasi = normalisasi.get_normalisasi()['n_data_normalisasi']
    n_list_data_kernel_view = []
    n_list_data_kernel = []

    s = 2

    for i, x in enumerate(n_data_normalisasi):
        n_data_kernel_view = []
        n_data_kernel = []

        for j, y in enumerate(n_data_normalisasi):
            n1 = math.pow((x['peminatprodi'] - y['peminatprodi']), 2)
            n2 = math.pow((x['rerataipk'] - y['rerataipk']), 2)
            n3 = math.pow((x['kelulusan'] - y['kelulusan']), 2)
            n4 = math.pow((x['jamkehadirandosen'] - y['jamkehadirandosen']), 2)
            n5 = math.pow((x['reratanilaidosen'] - y['reratanilaidosen']), 2)

            k = math.exp((-(n1 + n2 + n3 + n4 + n5)) / (2 * (math.pow(s, 2))))

            # if j == 0:
            #     n_data_kernel_view.append(x['namaprodi'])

            n_data_kernel_view.append(k)
            n_data_kernel.append(k)

        n_list_data_kernel_view.append(n_data_kernel_view)
        n_list_data_kernel.append(n_data_kernel)

    data_kernel = {
        'n_data_normalisasi': n_data_normalisasi,
        'n_list_data_kernel': n_list_data_kernel,
        'n_list_data_kernel_view': n_list_data_kernel_view
    }

    return data_kernel
