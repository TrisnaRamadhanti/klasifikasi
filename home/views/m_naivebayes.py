import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import KFold
from home.models import Data
import logging


def calculate_naivebayes(split):

    df = pd.DataFrame.from_records(Data.objects.all().values())

    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    y = df['label_kelas']
    y_kfold = df['label_kelas']

    df.drop(['id'], axis=1, inplace=True)
    df.drop(['label_kelas'], axis=1, inplace=True)
    df.drop(['semester_mulai'], axis=1, inplace=True)
    df.drop(['kode_prodi'], axis=1, inplace=True)
    df.drop(['tahun_smstr'], axis=1, inplace=True)
    df.drop(['nama_prodi'], axis=1, inplace=True)
    df.drop(['created_at'], axis=1, inplace=True)

    # Untuk mengambil data training
    x = df
    x_kfold = df

    # Jika ingin ambil data training dan test secara acak
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)

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

    # ---------------------------------------------------------------------------------------------------------------- #
    # Evaluasi Model
    x = x_kfold
    y = y_kfold

    scaler = StandardScaler()
    scaler.fit(x)

    x = scaler.transform(x)

    modelnb = GaussianNB()

    # Cara 1
    scores = []
    data_evaluasi = []

    cv = StratifiedKFold(n_splits=split)
    for train_index, test_index in cv.split(x, y):

        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]
        modelnb.fit(x_train, y_train)

        predictions = modelnb.predict(x_test)
        classification = classification_report(y_test, predictions, output_dict=True)
        print(classification)

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

        classification['1'] = data1
        classification['-1'] = data2

        evaluasi = [classification['1'], classification['-1']]
        data_evaluasi.append({
            'evaluasi': evaluasi,
            'accuracy': classification['accuracy']
        })

        print(classification['1'])
        print(classification['-1'])
        print('------------------')

        scores.append(modelnb.score(x_test, y_test))

    # Cara 2
    # kfold_scores = cross_val_score(modelnb, x, y, cv=2)
    # kfold_predict = cross_val_predict(modelnb, x, y, cv=2)

    print('Evaluasi Scores')
    print(np.mean(scores))
    print("-----------------------")

    print(data_evaluasi)

    data_naive_bayes = {
        'data_training': x_train,
        'data_testing': x_test,
        'probalitas': predictions_prob,
        'prediksi': predictions,
        'confusion': confusion,
        'report': classification,
        'scores': scores,
        'scores_mean': np.mean(scores),
        'data_evaluasi': data_evaluasi
    }

    return data_naive_bayes
