from django.views.generic import ListView
from home.views import t_svm_seq


class IndexView(ListView):
    template_name = 'home_svm_seq.html'
    context_object_name = 'data'

    def get_queryset(self):
        n_list_data_kernel_view = t_svm_seq.get_kernel()['n_list_data_kernel_view']

        context = {
            'n_list_data_kernel_view': n_list_data_kernel_view
        }

        return context

