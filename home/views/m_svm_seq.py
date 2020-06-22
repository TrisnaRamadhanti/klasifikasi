import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from home.models import Data


def calculate_svm_seq(const, max_iterasi, gamma, split):

    df = pd.DataFrame.from_records(Data.objects.all().values())

    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    x = df.iloc[:, 5:10]
    y = df['label_kelas']

    # ---------------------------------------------------------------------------------------------------------------- #
    # Evaluasi Model

    scaler = StandardScaler()
    scaler.fit(x)

    x = scaler.transform(x)

    svclassifier = SVC(kernel='rbf', C=const, max_iter=max_iterasi, gamma=gamma, probability=True)

    # Cara 1
    scores = []
    data_evaluasi = []

    cv = StratifiedKFold(n_splits=split, shuffle=True, random_state=42)
    for train_index, test_index in cv.split(x, y):

        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]
        svclassifier.fit(x_train, y_train)

        predictions = svclassifier.predict(x_test)
        classification = classification_report(y_test, predictions, output_dict=True)

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

        classification['1'] = data1
        classification['-1'] = data2

        evaluasi = [classification['1'], classification['-1']]
        data_evaluasi.append({
            'evaluasi': evaluasi,
            'accuracy': classification['accuracy']
        })

        scores.append(svclassifier.score(x_test, y_test))

    # Cara 2
    # kfold_scores = cross_val_score(modelnb, x, y, cv=2)
    # kfold_predict = cross_val_predict(modelnb, x, y, cv=2)

    data_svm = {
        'scores': scores,
        'scores_mean': np.mean(scores),
        'data_evaluasi': data_evaluasi
    }

    return data_svm
