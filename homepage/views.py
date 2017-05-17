from django.shortcuts import render
from homepage.models import *
# Create your views here.


def index(request):

    # context = {'lang': lang, 'right_data': right_data, 'text2': text2}
    return render(request, 'homepage/index.html', {})


def catalog(request):
    data = Catalog.objects.all().order_by('-sorting')
    context = {'data': data}
    return render(request, 'homepage/catalog.html', context)
