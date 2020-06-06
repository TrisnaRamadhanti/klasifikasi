import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

from home.models import Data
from home.views.svm_smo import SVM


def calculate_svm_smo(epsilon, C, max_iter, split):

    df = pd.DataFrame.from_records(Data.objects.all().values())

    df['label_kelas'] = df['label_kelas'].apply(lambda l: 1 if l == 'Berkembang' else -1)

    y = df['label_kelas']
    y_kfold = df['label_kelas']

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

    svm = SVM(max_iter=max_iter, kernel_type='linear', C=C, epsilon=epsilon)
    svm.fit(np.array(x_train), np.array(y_train))

    # predictions_prob = svm.predict_proba(x_test)

    predictions = svm.predict(x_test)

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
    # print('Prediksi Probabilitas')
    # print(predictions_prob)
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

    svm = SVM(max_iter=max_iter, kernel_type='linear', C=C, epsilon=epsilon)

    # Cara 1
    scores = []
    cv = StratifiedKFold(n_splits=split, shuffle=True, random_state=42)
    for train_index, test_index in cv.split(x, y):
        x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]
        svm.fit(np.array(x_train), np.array(y_train))

        predictions = svm.predict(x_test)
        # print("Predictions: ", predictions)

        # scores.append(svm.score(x_test, y_test))

    # Cara 2
    # kfold_scores = cross_val_score(modelnb, x, y, cv=2)
    # kfold_predict = cross_val_predict(modelnb, x, y, cv=2)

    # print('Evaluasi Scores')
    # print(np.mean(scores))
    # print("-----------------------")

    data_svm = {
        'data_training': x_train,
        'data_testing': x_test,
        # 'probalitas': predictions_prob,
        'prediksi': predictions,
        'confusion': confusion,
        'report': classification,
        'scores': scores,
        'scores_mean': '-',
        # 'pesan': pesan
    }

    return data_svm
