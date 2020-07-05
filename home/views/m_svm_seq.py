import numpy as np
import pandas as pd
# Proses import classification_report dari library scikit-learn
# Library untuk evaluasi performasi  
from sklearn.metrics import classification_report
# Proses import stratifiedKFold dari library scikit-learn 
# untuk pembagian data training dan data testing
from sklearn.model_selection import StratifiedKFold
# proses impor class StandardScaler dari library scikit-learn dan sublibrary preprocessing
from sklearn.preprocessing import StandardScaler
# import library untuk svm dari scikit-learn
from sklearn.svm import SVC

from home.models import Data


def calculate_svm_seq(tahun, const, max_iterasi, gamma, split):

<<<<<<< HEAD
    # Variabel untuk memanggil data dari fungsi get_normalisasi
    # data hasil normalisasi
    data = get_normalisasi()
=======
    df = pd.DataFrame.from_records(Data.objects.filter(tahun_smstr=tahun).values())

    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    x = df.iloc[:, 5:10]
    y = df['label_kelas']

    # ---------------------------------------------------------------------------------------------------------------- #
    # Evaluasi Model

    scaler = StandardScaler()
    scaler.fit(x)
>>>>>>> 892d572af493c3d4e65d2433682b61a564f3bd78

    # Deklarasi data 
    x = data['x']   # Parameter hasil normalisasi 
    y = data['y']   # label data

    # Membuat classifier SCV dengan parameter input dan kernal rbf
    svclassifier = SVC(kernel='rbf', C=const, max_iter=max_iterasi, gamma=gamma, probability=True)

    # Membuat array untuk menyimpan data dari perulangan kfold
    scores = []              # Menyimpan hasil akurasi masing-masing iterasi
    data_evaluasi = []       # Menyimpan data evaluasi masing-masing iterasi

    # Memanggil fungsi stratifiedKfold dengan parameter input nilai K
    cv = StratifiedKFold(n_splits=split)

    # Iterasi / pembagian data
    # Membuat indeks untuk membagi data menjadi data training dan testing
    for train_index, test_index in cv.split(x, y):

        # mendeklarasikan data training dan testing dari pembagian data 
        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]

        # Membuat model svm dengan 
        # data x (parameter) data training dan y (label) data training
        # Proses training
        svclassifier.fit(x_train, y_train)

        # hasil prediksi data testing
        predictions = svclassifier.predict(x_test)

        # Untuk mendapatkan evaluasi dari klasifikasi
        # Dengan parameter : label testing, hasil prediksi, output_dict 
        classification = classification_report(y_test, predictions, output_dict=True)

<<<<<<< HEAD
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
=======
        evaluasi = []

        if '1' in classification:
            data1 = {
                'label': 'Berkembang',
                'precision': classification['1']['precision'],
                'recall': classification['1']['recall'],
                'f1_score': classification['1']['f1-score']
            }
            evaluasi.append(data1)

        if '-1' in classification:
            data2 = {
                'label': 'Belum Berkembang',
                'precision': classification['-1']['precision'],
                'recall': classification['-1']['recall'],
                'f1_score': classification['-1']['f1-score']
            }
            evaluasi.append(data2)

>>>>>>> 892d572af493c3d4e65d2433682b61a564f3bd78
        data_evaluasi.append({
            'evaluasi': evaluasi,
            'accuracy': classification['accuracy']
        })

        scores.append(svclassifier.score(x_test, y_test))

    data_svm = {
        'scores': scores,
        'scores_mean': np.mean(scores),
        'data_evaluasi': data_evaluasi
    }

    return data_svm

def get_normalisasi():

    df = pd.DataFrame.from_records(Data.objects.all().values())

    # Untuk merubah label kelas menjadi angka 1 dan -1
    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    # Mengambil data dari urutan ke 5 sampai ke 10 
    # variabel x merupakan parameter data, mengambil parameter data  
    x = df.iloc[:, 5:10]

    # variabel y merupakan label kelas yang sudah dirubah menjadi angka
    y = df['label_kelas']

    # Proses preprocessing

    # variabel proses dari StandarScaler
    scaler = StandardScaler()

    # menghitung nilai rataan dan standar deviasi dari data variabel x 
    # untuk NANTI-nya digunakan saat proses scaling. 
    scaler.fit(x)

    # hasil perhitungan rataan dan standar deviasi sebelumnya (dari ‘fit’) untuk diterapkan ke data
    x = scaler.transform(x)

    # Membuat array untuk menyimpan variabel data x dan y 
    data = {
        'x': x,
        'y': y
    }

    return data

