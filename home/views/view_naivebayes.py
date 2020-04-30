from django.views.generic import ListView
from home.views import t_naivebayes
from home.views import m_naivebayes

class IndexView(ListView):
    template_name = 'home_naivebayes.html'
    context_object_name = 'data'

    def get_queryset(self):
        data_testing = m_naivebayes.calculate_naivebayes()['data_testing']
        probalitas = m_naivebayes.calculate_naivebayes()['probalitas']
        prediksi = m_naivebayes.calculate_naivebayes()['prediksi']
        pesan = m_naivebayes.calculate_naivebayes()['pesan']

        context = {
            'data_testing': data_testing,
            'probalitas': probalitas,
            'prediksi': prediksi,
            'pesan': pesan
        }


        # data_peluang = t_naivebayes.calculate_naivebayes()['data_peluang']
        # data_mean = t_naivebayes.calculate_naivebayes()['data_mean']
        # data_std_deviasi = t_naivebayes.calculate_naivebayes()['data_std_deviasi']
        # data_gaussian = t_naivebayes.calculate_naivebayes()['data_gaussian']
        # data_prob_posterior = t_naivebayes.calculate_naivebayes()['data_prob_posterior']
        # result = t_naivebayes.calculate_naivebayes()['result']

        # context = {
        #     'data_peluang': data_peluang,
        #     'data_mean': data_mean,
        #     'data_std_deviasi': data_std_deviasi,
        #     'data_gaussian': data_gaussian,
        #     'data_prob_posterior': data_prob_posterior,
        #     'result': result
        # }

        return context

