import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

from home.models import Data
from chefboost import Chefboost as cf


def calculate_decisiontree(split):

    df = pd.DataFrame.from_records(Data.objects.all().values())

    df.rename(columns={'label_kelas': 'Decision'}, inplace=True)

    y = df['Decision']
    y_kfold = df['Decision']

    df.drop(['semester_mulai'], axis=1, inplace=True)
    df.drop(['kode_prodi'], axis=1, inplace=True)
    df.drop(['tahun_smstr'], axis=1, inplace=True)
    df.drop(['nama_prodi'], axis=1, inplace=True)
    df.drop(['created_at'], axis=1, inplace=True)

    # Untuk mengambil data training
    x = df
    x_kfold = df

    # Evaluasi Model
    x = x_kfold
    y = y_kfold

    scaler = StandardScaler()
    scaler.fit(x)

    x = scaler.transform(x)

    config = {'algorithm': 'C4.5'}

    # Cara 1
    scores = []
    data_evaluasi = []

    cv = StratifiedKFold(n_splits=split, shuffle=True, random_state=42)
    for train_index, test_index in cv.split(x, y):
        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]
        model = cf.fit(df.copy(), config)

        predictions = cf.predict(model, x_test)
        # classification = classification_report(y_test, predictions, output_dict=True)

        # data1 = {
        #     'label': 'Berkembang',
        #     'precision': classification['1']['precision'],
        #     'recall': classification['1']['recall'],
        #     'f1_score': classification['1']['f1-score']
        # }
        # data2 = {
        #     'label': 'Belum Berkembang',
        #     'precision': classification['-1']['precision'],
        #     'recall': classification['-1']['recall'],
        #     'f1_score': classification['-1']['f1-score']
        # }
        #
        # classification['1'] = data1
        # classification['-1'] = data2
        #
        # evaluasi = [classification['1'], classification['-1']]
        # data_evaluasi.append(evaluasi)
        #
        # print(classification['1'])
        # print(classification['-1'])
        # print('------------------')

        print(test_index, predictions)

    # Cara 2
    # kfold_scores = cross_val_score(modelnb, x, y, cv=2)
    # kfold_predict = cross_val_predict(modelnb, x, y, cv=2)

    print('Evaluasi Scores')
    print(np.mean(scores))
    print("-----------------------")

    data_svm = {
        'scores': scores,
        'scores_mean': '-',
        'data_evaluasi': data_evaluasi
    }

    return data_svm
