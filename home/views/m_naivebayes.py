import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from home.models import Data
import logging


def calculate_naivebayes():

    df = pd.DataFrame.from_records(Data.objects.all().values())

    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    y = df['label_kelas']

    df.drop(['label_kelas'], axis=1, inplace=True)
    df.drop(['semester_mulai'], axis=1, inplace=True)
    df.drop(['kode_prodi'], axis=1, inplace=True)
    df.drop(['tahun_smstr'], axis=1, inplace=True)
    df.drop(['nama_prodi'], axis=1, inplace=True)
    df.drop(['created_at'], axis=1, inplace=True)

    # Untuk mengambil data training
    x = df

    # Jika ingin ambil data training dan test secara acak
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)

    # Membuat variabel baru yang menyimpan data training
    # x_train = x

    # Data testing
    # x_test = x.iloc[[0]]

    # Variabel untuk menyimpan label data training
    # y_train = y

    # Variabel untuk menyimpan label dari data testing
    # y_test = y.iloc[[0]]

    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    modelnb = GaussianNB()
    modelnb.fit(x_train, y_train)

    predictions_prob = modelnb.predict_proba(x_test)

    predictions = modelnb.predict(x_test)

    print('Data Training: ')
    print(x)
    print("-----------------------")
    print('Normalisasi Data Training')
    print(x_train)
    print("-----------------------")
    print('Normalisasi Data Testing')
    print(x_test)
    print("-----------------------")
    print('Label Data Training')
    print(y_train)
    print("-----------------------")
    print('Label Data Testing')
    print(y_test)
    print("-----------------------")
    print('Prediksi Probabilitas')
    print(predictions_prob)
    print("-----------------------")
    print('Prediksi')
    print(predictions)
    print("-----------------------")

    confusion = confusion_matrix(y_test, predictions)
    classification = classification_report(y_test, predictions)

    print(confusion)
    print(classification)

    # if predictions == 1:
    #     print('Berkembang'),
    #     pesan = 'Berkembang'
    # else:
    #     print('Belum Berkembang')
    #     pesan = 'Belum Berkembang'

    data_naive_bayes = {
        'data_training': x_train,
        'data_testing': x_test,
        'probalitas': predictions_prob,
        'prediksi': predictions,
        'confusion': confusion,
        'report': classification
        # 'pesan': pesan
    }

    return data_naive_bayes

