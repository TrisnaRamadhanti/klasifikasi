import pandas as pd
from chefboost import Chefboost as cf

from home.models import DataTesting
from home.views import normalisasi


# Proses import classification_report dari library scikit-learn
# Library untuk evaluasi performasi
# proses impor class StandardScaler dari library scikit-learn dan sublibrary preprocessing


def calculate_decisiontree():

    df = pd.DataFrame.from_records(DataTesting.objects.all().values())

    df.rename(columns={'label_kelas': 'Decision'}, inplace=True)

    df['peminat_prodi'] = df['peminat_prodi'].astype('float')
    df['rerata_ipk'] = df['rerata_ipk'].astype('float')
    df['kelulusan'] = df['kelulusan'].astype('int')
    df['jam_kehadiran_dosen'] = df['jam_kehadiran_dosen'].astype('float')
    df['rerata_nilai_dosen'] = df['rerata_nilai_dosen'].astype('float')

    for i, j in enumerate(df.to_numpy()):
        print(j[5:10])
        xnor = normalisasi.get_normalisasi(j[3], True)['data_normalisasi']

        x = pd.DataFrame({
            'peminat_prodi': xnor[:, 0].astype(float),
            'rerata_ipk': xnor[:, 1].astype(float),
            'kelulusan': xnor[:, 2].astype(float),
            'jam_kehadiran_dosen': xnor[:, 3].astype(float),
            'rerata_nilai_dosen': xnor[:, 4].astype(float),
            'Decision': xnor[:, 5]
        })

        config = {'algorithm': 'C4.5'}
        model = cf.fit(x, config)

        predictions = cf.predict(model, j[5:10])

        # Save Predictions to DB
        db_p = DataTesting.objects.filter(id=j[0])
        if len(db_p) > 0:
            db = db_p[0]
            db.label_kelas = predictions
            db.save()


