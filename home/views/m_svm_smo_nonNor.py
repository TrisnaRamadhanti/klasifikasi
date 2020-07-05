import numpy as np
import pandas as pd
# import library untuk svm-smo (Libsvm)
from libsvm.svmutil import *
# Proses import classification_report dari library scikit-learn
# Library untuk evaluasi performasi
from sklearn.metrics import classification_report
# Proses import stratifiedKFold dari library scikit-learn 
# untuk pembagian data training dan data testing
from sklearn.model_selection import StratifiedKFold

from home.models import Data


def calculate_svm_smo(tahun, epsilon, C, split):

     # Variabel untuk memanggil data dari fungsi get_data
    data = get_normalisasi()

    # Deklarasi data 
    x = data['x']   # Parameter hasil normalisasi 
    y = data['y']   # label data

    # Deklarasi parameter yang digunakan untuk smo
    param = svm_parameter()
    param.kernel_type = RBF
    param.eps = epsilon
    param.C = C

    # Membuat array untuk menyimpan data dari perulangan kfold
    scores = []             # Menyimpan hasil akurasi masing-masing iterasi
    data_evaluasi = []      # Menyimpan data evaluasi masing-masing iterasi

    # Memanggil fungsi stratifiedKfold dengan parameter input nilai K
    cv = StratifiedKFold(n_splits=split)

    # Iterasi / pembagian data
    # Membuat indeks untuk membagi data menjadi data training dan testing
    for train_index, test_index in cv.split(x, y):

        # mendeklarasikan data training dan testing dari pembagian data 
        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]
        
        # Proses training 
        # Terdapat pada dokumentasi c4.5 
        prob = svm_problem(np.array(y_train), np.array(x_train))

        m = svm_train(prob, param)

        # hasil prediksi data testing
        predictions = svm_predict(np.array(y_test), np.array(x_test), m)

        # Untuk mendapatkan evaluasi dari klasifikasi
        # Dengan parameter : label testing, hasil prediksi, output_dict 
        classification = classification_report(y_test, predictions[0], output_dict=True)

        # Hasil evaluasi masing-masing label
        # Dengan evaluasi precision, recall, dan f1 score
        data1 = {
            'label': 'Berkembang',
            'precision': classification['1']['precision'],
            'recall': classification['1']['recall'],
            'f1_score': classification['1']['f1-score']
        }
        data2 = {
            'label': 'Belum Berkembang',
            'precision': classification['-1']['precision'],
            'recall': classification['-1']['recall'],
            'f1_score': classification['-1']['f1-score']
        }

        # Membuat variabel array yang berisikan data hasil evaluasi 
        # masing-masing label
        classification['1'] = data1
        classification['-1'] = data2

        # Menambahkan objek ke list 
        # Menambahkan elemen pada indeks terakhir
        evaluasi = [classification['1'], classification['-1']]
        data_evaluasi.append({
            'evaluasi': evaluasi,
            'accuracy': classification['accuracy']
        })

        # Method hasil akurasi dengan parameter data testing dan label data testing 
        scores.append(classification['accuracy'])

    data_svm = {
        'scores': scores,
        'scores_mean': np.mean(scores),
        'data_evaluasi': data_evaluasi
    }

    return data_svm

def get_data():

    df = pd.DataFrame.from_records(Data.objects.all().values())

    # Untuk merubah label kelas menjadi angka 1 dan -1
    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    # Mengambil data dari urutan ke 5 sampai ke 10 
    # variabel x merupakan parameter data 
    x = df.iloc[:, 5:10]

    # variabel y merupakan label kelas yang sudah dirubah menjadi angka
    y = df['label_kelas']

   

    # Membuat array untuk menyimpan variabel data x dan y 
    data = {
        'x': x,
        'y': y
    }

    return data
