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

    df.drop(['id'], axis=1, inplace=True)
    df.drop(['semester_mulai'], axis=1, inplace=True)
    df.drop(['kode_prodi'], axis=1, inplace=True)
    df.drop(['tahun_smstr'], axis=1, inplace=True)
    df.drop(['nama_prodi'], axis=1, inplace=True)
    df.drop(['created_at'], axis=1, inplace=True)

    df_copy = df.copy()
    y = df['Decision']

    # Test
    df.drop(['Decision'], axis=1, inplace=True)
    x = df.to_numpy()

    config = {'algorithm': 'C4.5'}
    model = cf.fit(df_copy, config)

    # Cara 1
    scores = []
    data_evaluasi = []

    cv = StratifiedKFold(n_splits=split, shuffle=True, random_state=42)
    for train_index, test_index in cv.split(x, y):

        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]

        predictions_list = []

        for i, z in enumerate(x_test.tolist()):
            predictions = cf.predict(model, z)
            predictions_list.append(predictions)

        print(x_test)
        print("----------------------------------")
        print(predictions_list)

        classification = classification_report(y_test, predictions_list, output_dict=True)

        data1 = {
            'label': 'Berkembang',
            'precision': classification['Berkembang']['precision'],
            'recall': classification['Berkembang']['recall'],
            'f1_score': classification['Berkembang']['f1-score']
        }
        data2 = {
            'label': 'Belum Berkembang',
            'precision': classification['Belum Berkembang']['precision'],
            'recall': classification['Belum Berkembang']['recall'],
            'f1_score': classification['Belum Berkembang']['f1-score']
        }

        classification['Berkembang'] = data1
        classification['Belum Berkembang'] = data2

        evaluasi = [classification['Berkembang'], classification['Belum Berkembang']]
        data_evaluasi.append({
            'evaluasi': evaluasi,
            'accuracy': classification['accuracy']
        })

        # print(classification['Berkembang'])
        # print(classification['Belum Berkembang'])
        # print('------------------')

        # print(test_index, predictions)

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
