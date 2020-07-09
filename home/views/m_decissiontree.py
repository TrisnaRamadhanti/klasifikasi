import numpy as np
import pandas as pd
# Import library untuk c4.5
from chefboost import Chefboost as cf
# Proses import classification_report dari library scikit-learn
# Library untuk evaluasi performasi
from sklearn.metrics import classification_report
# proses impor class StandardScaler dari library scikit-learn dan sublibrary preprocessing
from sklearn.model_selection import StratifiedKFold

from home.models import Data
from home.views import normalisasi


def calculate_decisiontree(split, tahun):

    # Proses pengambilan data 
    df = pd.DataFrame.from_records(Data.objects.filter(tahun_smstr=tahun).values())

    # Merubah naman kolom label_kelas -> Decision
    df.rename(columns={'label_kelas': 'Decision'}, inplace=True)

    df['peminat_prodi'] = df['peminat_prodi'].astype('float')
    df['rerata_ipk'] = df['rerata_ipk'].astype('float')
    df['kelulusan'] = df['kelulusan'].astype('int')
    df['jam_kehadiran_dosen'] = df['jam_kehadiran_dosen'].astype('float')
    df['rerata_nilai_dosen'] = df['rerata_nilai_dosen'].astype('float')

    # Normalisasi
    xNor = normalisasi.get_normalisasi(tahun)['data_normalisasi']

    x = pd.DataFrame({
        'peminat_prodi': xNor[:, 0],
        'rerata_ipk': xNor[:, 1],
        'kelulusan': xNor[:, 2],
        'jam_kehadiran_dosen': xNor[:, 3],
        'rerata_nilai_dosen': xNor[:, 4],
        'Decision': xNor[:, 5]
    })

    # Untuk setting library. dengan algoritma c4.5
    config = {'algorithm': 'C4.5'}
    # Untuk training modelnya 
    # Dengan parameter datanya 
    # model = cf.fit(df.iloc[:, 5:11].copy(), config)
    model = cf.fit(x, config)

    x = df.iloc[:, 5:10].to_numpy()
    y = df['Decision']

    # Membuat array untuk menyimpan data dari perulangan kfold
    scores = []             # Menyimpan hasil akurasi masing-masing iterasi
    data_evaluasi = []      # Menyimpan data evaluasi masing-masing iterasi

    # Memanggil fungsi stratifiedKfold dengan parameter input nilai K
    cv = StratifiedKFold(n_splits=split, shuffle=True, random_state=42)

    # Iterasi / pembagian data
    # Membuat indeks untuk membagi data menjadi data training dan testing
    for train_index, test_index in cv.split(x, y):

        # mendeklarasikan data training dan testing dari pembagian data
        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]

        # ------ Proses training ----

        # Membuat array untuk menyimpan prediksi
        predictions_list = []

        for i, z in enumerate(x_test.tolist()):
            predictions = cf.predict(model, z)
            predictions_list.append(predictions)

        # Untuk mendapatkan evaluasi dari klasifikasi
        # Dengan parameter : label testing, hasil prediksi, output_dict
        classification = classification_report(y_test, predictions_list, output_dict=True)

        # Hasil evaluasi masing-masing label
        # Dengan evaluasi precision, recall, dan f1 score
        evaluasi = []
        if 'Berkembang' in classification:
            data1 = {
                'label': 'Berkembang',
                'precision': classification['Berkembang']['precision'],
                'recall': classification['Berkembang']['recall'],
                'f1_score': classification['Berkembang']['f1-score']
            }
            evaluasi.append(data1)

        if 'Belum Berkembang' in classification:
            data2 = {
                'label': 'Belum Berkembang',
                'precision': classification['Belum Berkembang']['precision'],
                'recall': classification['Belum Berkembang']['recall'],
                'f1_score': classification['Belum Berkembang']['f1-score']
            }
            evaluasi.append(data2)

        data_evaluasi.append({
            'evaluasi': evaluasi,
            'accuracy': classification['accuracy']
        })

        scores.append(classification['accuracy'])

    data_svm = {
        'scores': scores,
        'scores_mean': np.mean(scores),
        'data_evaluasi': data_evaluasi
    }

    return data_svm
