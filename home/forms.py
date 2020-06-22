from django import forms
from django.forms import TextInput

from .models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


class TrainingSvmSeqForm(forms.Form):
    # sigma = forms.CharField(label='Sigma', required=True, max_length=100,
    #                         widget=TextInput(attrs={'type': 'number'}),
    #                         error_messages={'required': "Sigma"})
    # lamda = forms.CharField(label='Lambda', required=True, max_length=100,
    #                         widget=TextInput(attrs={'type': 'number'}),
    #                         error_messages={'required': "Lambda"})
    constant = forms.CharField(label='Constant', required=True, max_length=100,
                               widget=TextInput(attrs={'type': 'number'}),
                               error_messages={'required': "Constant"})
    gamma = forms.CharField(label='Gamma', required=True, max_length=100,
                            widget=TextInput(attrs={'type': 'number'}),
                            error_messages={'required': "Gamma"})
    iterasi = forms.CharField(label='Iterasi', required=True, max_length=100,
                              widget=TextInput(attrs={'type': 'number'}),
                              error_messages={'required': "Iterasi"})
    k_fold = forms.CharField(label='KFold (Split)', required=True, max_length=100,
                             widget=TextInput(attrs={'type': 'number'}),
                             error_messages={'required': "Masukkan KFold (Split)"})


class TrainingSvmSmoForm(forms.Form):
    constant = forms.CharField(label='Constant', required=True, max_length=100,
                               widget=TextInput(attrs={'type': 'number'}),
                               error_messages={'required': "Constant"})
    # iterasi = forms.CharField(label='Iterasi', required=True, max_length=100,
    #                           widget=TextInput(attrs={'type': 'number'}),
    #                           error_messages={'required': "Iterasi"})
    epsilon = forms.CharField(label='Tolerance (Nilai Error / E)', required=True, max_length=100,
                              widget=TextInput(attrs={'type': 'number'}),
                              error_messages={'required': "Iterasi"})
    k_fold = forms.CharField(label='KFold (Split)', required=True, max_length=100,
                             widget=TextInput(attrs={'type': 'number'}),
                             error_messages={'required': "Masukkan KFold (Split)"})


class TrainingNaiveBayesForm(forms.Form):
    k_fold = forms.CharField(label='KFold (Split)', required=True, max_length=100,
                             widget=TextInput(attrs={'type': 'number'}),
                             error_messages={'required': "Masukkan KFold (Split)"})


class TrainingDecissionTreeForm(forms.Form):
    k_fold = forms.CharField(label='KFold (Split)', required=True, max_length=100,
                             widget=TextInput(attrs={'type': 'number'}),
                             error_messages={'required': "Masukkan KFold (Split)"})
