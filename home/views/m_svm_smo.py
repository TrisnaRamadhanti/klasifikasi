import numpy as np
import pandas as pd
from libsvm.svmutil import *
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

from home.models import Data


def calculate_svm_smo(tahun, epsilon, C, split):

    df = pd.DataFrame.from_records(Data.objects.filter(tahun_smstr=tahun).values())

    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    x = df.iloc[:, 5:10]
    y = df['label_kelas']

    # ---------------------------------------------------------------------------------------------------------------- #
    # Evaluasi Model

    scaler = StandardScaler()
    scaler.fit(x)

    x = scaler.transform(x)

    # svm = SVM(max_iter=max_iter, kernel_type='linear', C=C, epsilon=epsilon)

    param = svm_parameter()
    param.kernel_type = RBF
    param.eps = epsilon
    param.C = C

    # Cara 1
    scores = []
    data_evaluasi = []

    cv = StratifiedKFold(n_splits=split, shuffle=True, random_state=42)
    for train_index, test_index in cv.split(x, y):
        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]
        # svm.fit(np.array(x_train), np.array(y_train))

        prob = svm_problem(np.array(y_train), np.array(x_train))

        m = svm_train(prob, param)
        predictions = svm_predict(np.array(y_test), np.array(x_test), m)

        classification = classification_report(y_test, predictions[0], output_dict=True)

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
        'scores_mean': np.mean(scores),
        'data_evaluasi': data_evaluasi
    }

    return data_svm
