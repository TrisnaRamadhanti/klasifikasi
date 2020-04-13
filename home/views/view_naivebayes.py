from django.views.generic import ListView
from home.views import normalisasi


class IndexView(ListView):
    template_name = 'home_naivebayes.html'
    context_object_name = 'data'

    def get_queryset(self):
        data_normalisasi = normalisasi.get_normalisasi()['data_normalisasi']

        context = {
            'data_normalisasi': data_normalisasi
        }

        return context

