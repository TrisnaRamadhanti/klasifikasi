from django.shortcuts import render, redirect
from django.views.generic import ListView

from home.forms import TrainingNaiveBayesForm
from home.models import TrainingNaiveBayes
from home.views import m_naivebayes


class IndexView(ListView):
    template_name = 'home_naivebayes.html'
    context_object_name = 'data'

    def get_queryset(self):

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

                data_training = m_naivebayes.calculate_naivebayes(k_fold)
                
                scores = data_training['scores']
                scores_mean = data_training['scores_mean']
                data_evaluasi = data_training['data_evaluasi']

                context = {
                    'scores': scores,
                    'scores_mean': scores_mean,
                    'data_evaluasi': data_evaluasi,
                    'display': 'block',
                    'form': form
                }

                return render(request, self.template_name, {self.context_object_name: context})
            else:
                context = {
                    'scores': [],
                    'scores_mean': 0,
                    'data_evaluasi': [],
                    'display': 'none',
                    'form': form
                }

                return render(request, self.template_name, {self.context_object_name: context})
        else:
            return redirect('/login/')


class IndexViewNormalisasi(ListView):
    template_name = 'home_naivebayes_normalisasi.html'
    context_object_name = 'data'

    normalisasi = m_naivebayes.get_normalisasi()

    def get_queryset(self):

        context = {
            'scores': [],
        }

        return context
