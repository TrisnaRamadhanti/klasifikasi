from django.shortcuts import render, redirect
from django.views.generic import ListView

from home.forms import TrainingNaiveBayesForm
from home.models import TrainingNaiveBayes
from home.views import m_naivebayes_nonNor


class IndexView(ListView):
    template_name = 'home_naivebayes_nonNor.html'
    context_object_name = 'data'

    def get_queryset(self, **kwargs):

        tahun = self.kwargs['tahun']

        try:
            data = TrainingNaiveBayes.objects.get(id='1')
            if data is None:
                form = TrainingNaiveBayesForm()
            else:
                form = TrainingNaiveBayesForm(initial={
                    'k_fold': data.k_fold
                })
        except TrainingNaiveBayes.DoesNotExist:
            form = TrainingNaiveBayesForm()

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
        if 'username' in request.session:

            tahun = self.kwargs['tahun']

            form = TrainingNaiveBayesForm(request.POST)

            if form.is_valid():
                k_fold = int(form.cleaned_data['k_fold'])

                try:
                    param = TrainingNaiveBayes.objects.get(id='1')
                except TrainingNaiveBayes.DoesNotExist:
                    param = TrainingNaiveBayes()
                    param.id = '1'

                param.k_fold = k_fold
                param.save()

                data_training = m_naivebayes_nonNor.calculate_naivebayes(k_fold, tahun)
                
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
        else:
            return redirect('/login/')

