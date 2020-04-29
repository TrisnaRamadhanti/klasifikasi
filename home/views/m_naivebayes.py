import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
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

    x = df

    # Jika ingin ambil data training dan test secara acak
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)

    x_train = x
    x_test = x.iloc[[0]]

    y_train = y
    y_test = y.iloc[[0]]

    modelnb = GaussianNB()

    nbtrain = modelnb.fit(x_train, y_train)

    p = nbtrain.predict_proba(x_test)

    y_pred = nbtrain.predict(x_test)

    print(x)
    print(x_train)
    print(x_test)
    print(y_train)
    print(y_test)
    print(p)
    print(y_pred)
