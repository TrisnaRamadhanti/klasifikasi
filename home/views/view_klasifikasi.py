from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get

from home.forms import DataForm
from home.models import DataTesting


class IndexView(ListView):
    template_name = 'home_klasifikasi.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataTesting.objects.all()


class DataDetailView(DetailView):
    model = DataTesting
    template_name = 'data-detail.html'


def beranda(request):
    if 'username' in request.session:
        return render(request, 'index.html')
    else:
        return redirect('/login/')


def create(request):
    if 'username' in request.session:
        form = DataForm()

        if request.method == 'POST':
            if request.POST.get("input_excel"):
                try:
                    excel_file = request.FILES['file-excel']
                except MultiValueDictKeyError:
                    return render(request, 'create.html', {'form': form})

                if str(excel_file).split('.')[-1] == 'xls':
                    data = xls_get(excel_file, column_limit=5)
                elif str(excel_file).split('.')[-1] == 'xlsx':
                    data = xlsx_get(excel_file, column_limit=5)
                else:
                    return render(request, 'create.html', {'form': form})

                if data is not None:
                    # save_excel_to_db(data)
                    return redirect('home:data_view')

            else:
                form = DataForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('home:data_view')

        return render(request, 'create.html', {'form': form})
    else:
        return redirect('/login/')


def edit(request, pk, template_name='edit.html'):
    if 'username' in request.session:
        data = get_object_or_404(DataTesting, pk=pk)
        form = DataForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home:data_view')
        return render(request, template_name, {'form': form})
    else:
        return redirect('/login/')


def delete(request, pk, template_name='confirm_delete.html'):
    if 'username' in request.session:
        contact = get_object_or_404(DataTesting, pk=pk)
        if request.method == 'POST':
            contact.delete()
            return redirect('home:data_view')
        return render(request, template_name, {'object': contact})
    else:
        return redirect('/login/')