import numpy as np
import pandas as pd
from chefboost import Chefboost as cf
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold

from home.models import Data


def calculate_decisiontree(split):

    df = pd.DataFrame.from_records(Data.objects.all().values())

    df.rename(columns={'label_kelas': 'Decision'}, inplace=True)

    df['peminat_prodi'] = df['peminat_prodi'].astype('float')
    df['rerata_ipk'] = df['rerata_ipk'].astype('float')
    df['kelulusan'] = df['kelulusan'].astype('int')
    df['jam_kehadiran_dosen'] = df['jam_kehadiran_dosen'].astype('float')
    df['rerata_nilai_dosen'] = df['rerata_nilai_dosen'].astype('float')

    config = {'algorithm': 'C4.5'}
    model = cf.fit(df.iloc[:, 5:11].copy(), config)

    x = df.iloc[:, 5:10].to_numpy()
    y = df['Decision']

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

        scores.append(classification['accuracy'])

    # Cara 2
    # kfold_scores = cross_val_score(modelnb, x, y, cv=2)
    # kfold_predict = cross_val_predict(modelnb, x, y, cv=2)

    data_svm = {
        'scores': scores,
        'data_evaluasi': data_evaluasi,
        'scores_mean': np.mean(scores)
    }

    return data_svm
