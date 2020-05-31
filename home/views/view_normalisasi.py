from django.views.generic import ListView

from home.views import normalisasi


class IndexView(ListView):
    template_name = 'data-normalisasi.html'
    context_object_name = 'data'

    def get_queryset(self):
        n_data_normalisasi = normalisasi.get_normalisasi()['n_data_normalisasi']

        context = {
            'n_data_normalisasi': n_data_normalisasi
        }

        return context

