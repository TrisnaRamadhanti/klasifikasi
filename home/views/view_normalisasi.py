from django.views.generic import ListView
from home.views import normalisasi
from home.views import m_naivebayes


class IndexView(ListView):
    template_name = 'data-normalisasi.html'
    context_object_name = 'data'

    def get_queryset(self):
        n_data_normalisasi = normalisasi.get_normalisasi()['n_data_normalisasi']

        m_naivebayes.calculate_naivebayes()

        context = {
            'n_data_normalisasi': n_data_normalisasi
        }

        return context

