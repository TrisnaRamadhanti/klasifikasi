"""ProjectSkripsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from home.views import view_data, view_normalisasi, view_naivebayes, view_svm_seq, view_svm_smo, view_decissiontree, \
    view_decissiontree_nonNor, view_svm_seq_nonNor, view_svm_smo_nonNor, view_naivebayes_nonNor, view_klasifikasi

app_name = 'home'

urlpatterns = [
    path('', view_data.beranda, name='home_view'),
    path('dataLatih/', view_data.DataLatih.as_view(), name='data_view'),
    path('<int:pk>/', view_data.DataDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', view_data.edit, name='edit'),
    path('create/', view_data.create, name='create'),
    path('delete/<int:pk>/', view_data.delete, name='delete'),

    # Normalisasi Data
    path('normalisasi/', view_normalisasi.IndexView.as_view(), name='normalisasi'),
    path('naivebayes/<int:tahun>/', view_naivebayes.IndexView.as_view(), name='naivebayes'),
    path('svmsequential/<int:tahun>/', view_svm_seq.IndexView.as_view(), name='svmsequential'),
    path('svmsmo/<int:tahun>/', view_svm_smo.IndexView.as_view(), name='svmsmo'),
    path('decissiontree/<int:tahun>/', view_decissiontree.IndexView.as_view(), name='decissiontree'),

    # Non Normalisasi Data
    path('decissiontree_nonNor/<int:tahun>/', view_decissiontree_nonNor.IndexView.as_view(), name='decissiontree_nonNor'),
    path('svmsequential_nonNor/<int:tahun>/', view_svm_seq_nonNor.IndexView.as_view(), name='svmsequential_nonNor'),
    path('svmsmo_nonNor/<int:tahun>/', view_svm_smo_nonNor.IndexView.as_view(), name='svmsmo_nonNor'),
    path('naivebayes_nonNor/<int:tahun>/', view_naivebayes_nonNor.IndexView.as_view(), name='naivebayes_nonNor'),

    path('klasifikasi/', view_klasifikasi.IndexView.as_view(), name='klasifikasi'),
    path('klasifikasi/<int:pk>/', view_klasifikasi.DataDetailView.as_view(), name='klasifikasi_detail'),
    path('klasifikasi_create/', view_klasifikasi.create, name='klasifikasi_create'),
    path('klasifikasi_edit/<int:pk>/', view_klasifikasi.edit, name='klasifikasi_edit'),
    path('klasifikasi_delete/<int:pk>/', view_klasifikasi.delete, name='klasifikasi_delete'),
]
