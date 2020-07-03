import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

from home.models import Data


def calculate_naivebayes(split, tahun):

    data = get_normalisasi(tahun)
    x = data['x']
    y = data['y']

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

        evaluasi = []

        if '1' in classification:
            data1 = {
                'label': 'Berkembang',
                'precision': classification['1']['precision'],
                'recall': classification['1']['recall'],
                'f1_score': classification['1']['f1-score'],
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

        data_evaluasi.append({
            'evaluasi': evaluasi,
            'accuracy': classification['accuracy']
        })

        scores.append(modelnb.score(x_test, y_test))

    # Cara 2
    # kfold_scores = cross_val_score(modelnb, x, y, cv=2)
    # kfold_predict = cross_val_predict(modelnb, x, y, cv=2)

    data_naive_bayes = {
        'scores': scores,
        'scores_mean': np.mean(scores),
        'data_evaluasi': data_evaluasi
    }

    return data_naive_bayes


def get_normalisasi(tahun):

    df = pd.DataFrame.from_records(Data.objects.filter(tahun_smstr=tahun).values())

    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    x = df.iloc[:, 5:10]
    y = df['label_kelas']

    scaler = StandardScaler()
    scaler.fit(x)

    x = scaler.transform(x)

    data = {
        'x': x,
        'y': y
    }

    return data
