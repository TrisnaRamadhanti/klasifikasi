from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from home.forms import DataFormKlasifikasi
from home.models import DataTesting
from home.views import m_klasifikasi


class IndexView(ListView):
    template_name = 'home_klasifikasi.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataTesting.objects.all()


class DataDetailView(DetailView):
    model = DataTesting
    template_name = 'home_klasifikasi_detail.html'


def beranda(request):
    if 'username' in request.session:
        return render(request, 'index.html')
    else:
        return redirect('/login/')


def create(request):
    if 'username' in request.session:
        form = DataFormKlasifikasi()

        if request.method == 'POST':
            form = DataFormKlasifikasi(request.POST)
            if form.is_valid():
                form.save()

                # Predictions
                m_klasifikasi.calculate_decisiontree()

                return redirect('home:klasifikasi')

        return render(request, 'home_klasifikasi_create.html', {'form': form})
    else:
        return redirect('/login/')


def edit(request, pk, template_name='home_klasifikasi_edit.html'):
    if 'username' in request.session:
        data = get_object_or_404(DataTesting, pk=pk)
        form = DataFormKlasifikasi(request.POST or None, instance=data)
        if form.is_valid():
            form.save()

            # Predictions
            m_klasifikasi.calculate_decisiontree()

            return redirect('home:klasifikasi')
        return render(request, template_name, {'form': form})
    else:
        return redirect('/login/')


def delete(request, pk, template_name='confirm_delete.html'):
    if 'username' in request.session:
        contact = get_object_or_404(DataTesting, pk=pk)
        if request.method == 'POST':
            contact.delete()
            return redirect('home:klasifikasi')
        return render(request, template_name, {'object': contact})
    else:
        return redirect('/login/')
