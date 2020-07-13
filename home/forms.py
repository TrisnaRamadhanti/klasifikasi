from django import forms
from django.forms import TextInput

from .models import Data, DataTesting


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


class DataFormKlasifikasi(forms.ModelForm):
    class Meta:
        model = DataTesting
        fields = ['semester_mulai', 'kode_prodi', 'tahun_smstr', 'nama_prodi', 'peminat_prodi', 'rerata_ipk', 'kelulusan',
                  'jam_kehadiran_dosen', 'rerata_nilai_dosen']


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
