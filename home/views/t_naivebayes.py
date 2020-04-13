import math
from home.views import normalisasi


def calculate_naivebayes():
    n_data_normalisasi = normalisasi.get_normalisasi()['n_data_normalisasi']

    return n_data_normalisasi
