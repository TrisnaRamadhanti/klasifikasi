from django.shortcuts import render, redirect
from django.views.generic import ListView

from home.forms import TrainingDecissionTreeForm
from home.models import TrainingDecissionTree
from home.views import m_decissiontree


class IndexView(ListView):
    template_name = 'home_decissiontree.html'
    context_object_name = 'data'

    def get_queryset(self):

        try:
            data = TrainingDecissionTree.objects.get(id='1')
            if data is None:
                form = TrainingDecissionTreeForm()
            else:
                form = TrainingDecissionTreeForm(initial={
                    'k_fold': data.k_fold
                })
        except TrainingDecissionTree.DoesNotExist:
            form = TrainingDecissionTreeForm()

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
            form = TrainingDecissionTreeForm(request.POST)

            if form.is_valid():
                k_fold = int(form.cleaned_data['k_fold'])

                try:
                    param = TrainingDecissionTree.objects.get(id='1')
                except TrainingDecissionTree.DoesNotExist:
                    param = TrainingDecissionTree()
                    param.id = '1'

                param.k_fold = k_fold
                param.save()

                data_training = m_decissiontree.calculate_decisiontree(k_fold)
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

