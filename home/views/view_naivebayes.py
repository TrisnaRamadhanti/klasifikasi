from django.shortcuts import render, redirect, get_object_or_404
from home.models import Data
from home.forms import DataForm
from django.views.generic import ListView, DetailView
from home.views import view_normalisasi


class IndexView(ListView):
    template_name = 'data-normalisasi.html'
    context_object_name = 'data'

    def get_queryset(self):
        listdata = IndexView.


        context = {
            'n_data_normalisasi': n_data_normalisasi,
        }

        return context

