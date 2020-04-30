import pandas as pd
from django.views.generic import ListView

class IndexView(ListView):
    pd.read_excel('data.xlsx')