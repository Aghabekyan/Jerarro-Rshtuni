from django.shortcuts import render
from homepage.models import *
# Create your views here.


def index(request):

    # context = {'lang': lang, 'right_data': right_data, 'text2': text2}
    return render(request, 'homepage/index.html', {})


def catalog(request, category):
    data = Catalog.objects.filter(category__name=category).order_by('-sorting')
    print category
    context = {'data': data,
               'category': category}
    return render(request, 'homepage/catalog.html', context)
