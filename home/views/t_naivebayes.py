import math
from home.views import normalisasi
import logging


def calculate_naivebayes():

    data_normalisasi = normalisasi.get_normalisasi()['n_data_normalisasi']

    data_label = _get_label(data_normalisasi)

    data_peluang = _get_peluang(data_label, data_normalisasi)

    data_mean = _get_mean(data_label)

    data_std_deviasi = _get_std_deviasi(data_label, data_mean)

    data_gaussian = _get_gaussian(data_normalisasi, data_mean, data_std_deviasi)

    data_prob_posterior = _get_prob_posterior(data_peluang, data_gaussian)

    result = _get_result(data_prob_posterior)

    data_naivebayes = {
        'data_peluang': data_peluang,
        'data_mean': data_mean,
        'data_std_deviasi': data_std_deviasi,
        'data_gaussian': data_gaussian,
        'data_prob_posterior': data_prob_posterior,
        'result': result
    }

    return data_naivebayes


def _get_label(data_normalisasi):
    label_1 = []
    label_2 = []

    for i, x in enumerate(data_normalisasi):
        if x['label'] == '1':
            label_1.append(x)
        else:
            label_2.append(x)

    label = {
        'label_1': label_1,
        'label_2': label_2
    }

    return label


def _get_peluang(data_label, data_normalisasi):
    label_1 = data_label['label_1']
    label_2 = data_label['label_2']

    p1 = len(label_1) / len(data_normalisasi)
    p2 = len(label_2) / len(data_normalisasi)

    data_peluang = {
        'p1': p1,
        'p2': p2
    }

    return data_peluang


def _get_mean(data_label):
    label_1 = data_label['label_1']
    label_2 = data_label['label_2']

    mean_1 = {
        'peminatprodi': sum([float(i['peminatprodi']) for i in label_1]) / len(label_1),
        'rerataipk': sum([float(i['rerataipk']) for i in label_1]) / len(label_1),
        'kelulusan': sum([float(i['kelulusan']) for i in label_1]) / len(label_1),
        'jamkehadirandosen': sum([float(i['jamkehadirandosen']) for i in label_1]) / len(label_1),
        'reratanilaidosen': sum([float(i['reratanilaidosen']) for i in label_1]) / len(label_1)
    }

    mean_2 = {
        'peminatprodi': sum([float(i['peminatprodi']) for i in label_2]) / len(label_2),
        'rerataipk': sum([float(i['rerataipk']) for i in label_2]) / len(label_2),
        'kelulusan': sum([float(i['kelulusan']) for i in label_2]) / len(label_2),
        'jamkehadirandosen': sum([float(i['jamkehadirandosen']) for i in label_2]) / len(label_2),
        'reratanilaidosen': sum([float(i['reratanilaidosen']) for i in label_2]) / len(label_2)
    }

    data_mean = {
        'mean_1': mean_1,
        'mean_2': mean_2
    }

    return data_mean


def _get_std_deviasi(data_label, data_mean):
    label_1 = data_label['label_1']
    label_2 = data_label['label_2']

    mean_1 = data_mean['mean_1']
    mean_2 = data_mean['mean_2']

    std_dev_1 = {
        'peminatprodi': math.sqrt(sum([math.pow((float(i['peminatprodi']) - mean_1['peminatprodi']), 2) for i in label_1])) / (len(label_1) - 1),
        'rerataipk': math.sqrt(sum([math.pow((float(i['rerataipk']) - mean_1['rerataipk']), 2) for i in label_1])) / (len(label_1) - 1),
        'kelulusan': math.sqrt(sum([math.pow((float(i['kelulusan']) - mean_1['kelulusan']), 2) for i in label_1])) / (len(label_1) - 1),
        'jamkehadirandosen': math.sqrt(sum([math.pow((float(i['jamkehadirandosen']) - mean_1['jamkehadirandosen']), 2) for i in label_1])) / (len(label_1) - 1),
        'reratanilaidosen': math.sqrt(sum([math.pow((float(i['reratanilaidosen']) - mean_1['reratanilaidosen']), 2) for i in label_1])) / (len(label_1) - 1)
    }

    std_dev_2 = {
        'peminatprodi': math.sqrt(sum([math.pow((float(i['peminatprodi']) - mean_2['peminatprodi']), 2) for i in label_2])) / (len(label_2) - 1),
        'rerataipk': math.sqrt(sum([math.pow((float(i['rerataipk']) - mean_2['rerataipk']), 2) for i in label_2])) / (len(label_2) - 1),
        'kelulusan': math.sqrt(sum([math.pow((float(i['kelulusan']) - mean_2['kelulusan']), 2) for i in label_2])) / (len(label_2) - 1),
        'jamkehadirandosen': math.sqrt(sum([math.pow((float(i['jamkehadirandosen']) - mean_2['jamkehadirandosen']), 2) for i in label_2])) / (len(label_2) - 1),
        'reratanilaidosen': math.sqrt(sum([math.pow((float(i['reratanilaidosen']) - mean_2['reratanilaidosen']), 2) for i in label_2])) / (len(label_2) - 1)
    }

    data_std_deviasi = {
        'std_dev_1': std_dev_1,
        'std_dev_2': std_dev_2
    }

    return data_std_deviasi


def _get_gaussian(data_normalisasi, data_mean, data_std_deviasi):

    mean_1 = data_mean['mean_1']
    mean_2 = data_mean['mean_2']

    std_dev_1 = data_std_deviasi['std_dev_1']
    std_dev_2 = data_std_deviasi['std_dev_2']

    data_uji = data_normalisasi[0]

    pi = 3.14

    gaussian_1 = {
        'peminatprodi': (1 / math.sqrt(2*pi*math.pow(std_dev_1['peminatprodi'], 2))) *
                        (math.exp(-(math.pow((data_uji['peminatprodi'] - mean_1['peminatprodi']), 2) / (2 * (math.pow(std_dev_1['peminatprodi'], 2)))))),

        'rerataipk': (1 / math.sqrt(2*pi*math.pow(std_dev_1['rerataipk'], 2))) *
                     (math.exp(-(math.pow((data_uji['rerataipk'] - mean_1['rerataipk']), 2) / (2 * (math.pow(std_dev_1['rerataipk'], 2)))))),

        'kelulusan': (1 / math.sqrt(2*pi*math.pow(std_dev_1['kelulusan'], 2))) *
                     (math.exp(-(math.pow((data_uji['kelulusan'] - mean_1['kelulusan']), 2) / (2 * (math.pow(std_dev_1['kelulusan'], 2)))))),

        'jamkehadirandosen': (1 / math.sqrt(2*pi*math.pow(std_dev_1['jamkehadirandosen'], 2))) *
                             (math.exp(-(math.pow((data_uji['jamkehadirandosen'] - mean_1['jamkehadirandosen']), 2) / (2 * (math.pow(std_dev_1['jamkehadirandosen'], 2)))))),

        'reratanilaidosen': (1 / math.sqrt(2*pi*math.pow(std_dev_1['reratanilaidosen'], 2))) *
                            (math.exp(-(math.pow((data_uji['reratanilaidosen'] - mean_1['reratanilaidosen']), 2) / (2 * (math.pow(std_dev_1['reratanilaidosen'], 2))))))
    }

    gaussian_2 = {
        'peminatprodi': (1 / math.sqrt(2*pi*math.pow(std_dev_2['peminatprodi'], 2))) *
                        (math.exp(-(math.pow((data_uji['peminatprodi'] - mean_2['peminatprodi']), 2) / (2 * (math.pow(std_dev_2['peminatprodi'], 2)))))),

        'rerataipk': (1 / math.sqrt(2*pi*math.pow(std_dev_2['rerataipk'], 2))) *
                     (math.exp(-(math.pow((data_uji['rerataipk'] - mean_2['rerataipk']), 2) / (2 * (math.pow(std_dev_2['rerataipk'], 2)))))),

        'kelulusan': (1 / math.sqrt(2*pi*math.pow(std_dev_2['kelulusan'], 2))) *
                     (math.exp(-(math.pow((data_uji['kelulusan'] - mean_2['kelulusan']), 2) / (2 * (math.pow(std_dev_2['kelulusan'], 2)))))),

        'jamkehadirandosen': (1 / math.sqrt(2*pi*math.pow(std_dev_2['jamkehadirandosen'], 2))) *
                             (math.exp(-(math.pow((data_uji['jamkehadirandosen'] - mean_2['jamkehadirandosen']), 2) / (2 * (math.pow(std_dev_2['jamkehadirandosen'], 2)))))),

        'reratanilaidosen': (1 / math.sqrt(2*pi*math.pow(std_dev_2['reratanilaidosen'], 2))) *
                            (math.exp(-(math.pow((data_uji['reratanilaidosen'] - mean_2['reratanilaidosen']), 2) / (2 * (math.pow(std_dev_2['reratanilaidosen'], 2))))))
    }

    data_gaussian = {
        'gaussian_1': gaussian_1,
        'gaussian_2': gaussian_2
    }

    return data_gaussian


def _get_prob_posterior(data_peluang, data_gaussian):

    gaussian_1 = data_gaussian['gaussian_1']
    gaussian_2 = data_gaussian['gaussian_2']

    prob_posterior_1 = data_peluang['p1'] * gaussian_1['peminatprodi'] * gaussian_1['rerataipk'] * gaussian_1['kelulusan'] * gaussian_1['jamkehadirandosen'] * gaussian_1['reratanilaidosen']
    prob_posterior_2 = data_peluang['p2'] * gaussian_2['peminatprodi'] * gaussian_2['rerataipk'] * gaussian_2['kelulusan'] * gaussian_2['jamkehadirandosen'] * gaussian_2['reratanilaidosen']

    data_prob_posterior = {
        'prob_posterior_1': prob_posterior_1,
        'prob_posterior_2': prob_posterior_2
    }

    return data_prob_posterior


def _get_result(data_prob_posterior):

    result = max(data_prob_posterior['prob_posterior_1'], data_prob_posterior['prob_posterior_2'])

    return result
