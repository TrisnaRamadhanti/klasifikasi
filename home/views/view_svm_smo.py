from django.shortcuts import render
from django.views.generic import ListView

from home.forms import TrainingSvmSmoForm
from home.models import TrainingSvmSmo
from home.views import m_svm_smo


class IndexView(ListView):
    template_name = 'home_svm_smo.html'
    context_object_name = 'data'

    def get_queryset(self, **kwargs):

        tahun = self.kwargs['tahun']

        try:
            data = TrainingSvmSmo.objects.get(id='1')
            if data is None:
                form = TrainingSvmSmoForm()
            else:
                form = TrainingSvmSmoForm(initial={
                    'constant': data.constant,
                    'iterasi': data.iterasi,
                    'epsilon': data.epsilon,
                    'k_fold': data.k_fold
                })
        except TrainingSvmSmo.DoesNotExist:
            form = TrainingSvmSmoForm()

        context = {
            'tahun': tahun,
            'scores': [],
            'scores_mean': 0,
            'data_evaluasi': [],
            'display': 'none',
            'form': form
        }

        return context

    # Handle POST HTTP requests
    def post(self, request, *args, **kwargs):

        tahun = self.kwargs['tahun']

        form = TrainingSvmSmoForm(request.POST)

        if form.is_valid():
            constant = float(form.cleaned_data['constant'])
            epsilon = float(form.cleaned_data['epsilon'])
            k_fold = int(form.cleaned_data['k_fold'])

            try:
                param = TrainingSvmSmo.objects.get(id='1')
            except TrainingSvmSmo.DoesNotExist:
                param = TrainingSvmSmo()
                param.id = '1'

            param.constant = constant
            param.epsilon = epsilon
            param.k_fold = k_fold
            param.save()

            data_training = m_svm_smo.calculate_svm_smo(tahun, epsilon, constant, k_fold)
            scores = data_training['scores']
            scores_mean = data_training['scores_mean']
            data_evaluasi = data_training['data_evaluasi']

            context = {
                'tahun': tahun,
                'scores': scores,
                'scores_mean': scores_mean,
                'data_evaluasi': data_evaluasi,
                'display': 'block',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})
        else:
            context = {
                'tahun': tahun,
                'scores': [],
                'scores_mean': 0,
                'data_evaluasi': [],
                'display': 'none',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})

