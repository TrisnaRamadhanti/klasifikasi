import numpy as np
import pandas as pd
# Proses import classification_report dari library scikit-learn
from sklearn.metrics import classification_report
# Proses import Stratified dari library scikit-learn
from sklearn.model_selection import StratifiedKFold
# Proses import class GaussianNB dari library scikit-learn
from sklearn.naive_bayes import GaussianNB
# proses impor class StandardScaler dari library scikit-learn dan sublibrary preprocessing
from sklearn.preprocessing import StandardScaler
# memanggil class Data pada model
from home.models import Data


def calculate_naivebayes(split):

    # Membuat variabel untuk memanggil data dari fungsi get_normalisasi()
    # Data hasil normalisasi
    data = get_normalisasi()

    # Deklarasi variabel 
    x = data['x']
    y = data['y']

    # Mendeklarasikan GaussianNB
    # Mengaktifkan fungsi naive bayes
    modelnb = GaussianNB()

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

        # Membuat model naive bayes dengan 
        # data x (parameter) data training dan y (label) data training
        modelnb.fit(x_train, y_train)

        # hasil prediksi data testing
        predictions = modelnb.predict(x_test)

        # Untuk mendapatkan evaluasi dari klasifikasi
        # Dengan parameter : label testing, hasil prediksi, output_dict 
        classification = classification_report(y_test, predictions, output_dict=True)

        # Hasil evaluasi masing-masing label
        # Dengan evaluasi precision, recall, dan f1 score
        data1 = {
            'label': 'Berkembang',
            'precision': classification['1']['precision'],
            'recall': classification['1']['recall'],
            'f1_score': classification['1']['f1-score'],
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

        evaluasi = [classification['1'], classification['-1']]

        # Menambahkan objek ke list 
        # Menambahkan elemen pada indeks terakhir
        data_evaluasi.append({
            'evaluasi': evaluasi,
            'accuracy': classification['accuracy']
        })
        
        # Method hasil akurasi dengan parameter data testing dan label data testing 
        scores.append(modelnb.score(x_test, y_test))

    data_naive_bayes = {
        'scores': scores,
        'scores_mean': np.mean(scores),
        'data_evaluasi': data_evaluasi
    }

    return data_naive_bayes


# Fungsi untuk normalisasi data 

def get_normalisasi():

    df = pd.DataFrame.from_records(Data.objects.all().values())

    # Untuk merubah label kelas menjadi angka 1 dan -1
    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    # Mengambil data dari urutan ke 5 sampai ke 10 
    # variabel x merupakan parameter data 
    x = df.iloc[:, 5:10]

    # variabel y merupakan label kelas yang sudah dirubah menjadi angka
    y = df['label_kelas']

    # Proses preprocessing

    # variabel proses dari StandarScaler
    scaler = StandardScaler()

    # menghitung nilai rataan dan standar deviasi dari data variabel x 
    # untuk NANTI-nya digunakan saat proses scaling. 
    # Ia hanya menghitung nilai rataan dan standar deviasi saja
    scaler.fit(x)

    # hasil perhitungan rataan dan standar deviasi sebelumnya (dari ‘fit’) untuk diterapkan ke data
    x = scaler.transform(x)

    # Membuat array untuk menyimpan variabel data x dan y 
    data = {
        'x': x,
        'y': y
    }

    return data
