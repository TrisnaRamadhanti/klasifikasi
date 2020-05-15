from django.shortcuts import render
from django.views.generic import ListView

from home.forms import TrainingSvmSeqForm
from home.models import TrainingSvmSeq
from home.views import m_svm


class IndexView(ListView):
    template_name = 'home_svm_seq.html'
    context_object_name = 'data'

    def get_queryset(self):

        try:
            data = TrainingSvmSeq.objects.get(id='1')
            if data is None:
                form = TrainingSvmSeqForm()
            else:
                form = TrainingSvmSeqForm(initial={
                    # 'sigma': data.sigma,
                    # 'lamda': data.lamda,
                    'constant': data.constant,
                    'gamma': data.gamma,
                    'iterasi': data.iterasi,
                    'k_fold': data.k_fold
                })
        except TrainingSvmSeq.DoesNotExist:
            form = TrainingSvmSeqForm()

        context = {
            'scores': [],
            'scores_mean': 0,
            'display': 'none',
            'form': form
        }

        return context

    # Handle POST HTTP requests
    def post(self, request, *args, **kwargs):
        form = TrainingSvmSeqForm(request.POST)

        if form.is_valid():
            # sigma = float(form.cleaned_data['sigma'])
            # lamda = float(form.cleaned_data['lamda'])
            constant = float(form.cleaned_data['constant'])
            gamma = float(form.cleaned_data['gamma'])
            iterasi = int(form.cleaned_data['iterasi'])
            k_fold = int(form.cleaned_data['k_fold'])

            try:
                param = TrainingSvmSeq.objects.get(id='1')
            except TrainingSvmSeq.DoesNotExist:
                param = TrainingSvmSeq()
                param.id = '1'

            # param.sigma = sigma
            # param.lamda = lamda
            param.constant = constant
            param.gamma = gamma
            param.iterasi = iterasi
            param.k_fold = k_fold
            param.save()

            data_training = m_svm.calculate_svm(constant, iterasi, gamma, k_fold)
            scores = data_training['scores']
            scores_mean = data_training['scores_mean']

            context = {
                'scores': scores,
                'scores_mean': scores_mean,
                'display': 'block',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})
        else:
            context = {
                'scores': [],
                'scores_mean': 0,
                'display': 'none',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})

