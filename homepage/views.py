from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from homepage.models import *
# Create your views here.


def index(request):

    # context = {'lang': lang, 'right_data': right_data, 'text2': text2}
    return render(request, 'homepage/index.html', {})


def catalog(request, category):
    catalog_data = Catalog.objects.filter(category__name=category).order_by('-sorting')

    paginator = Paginator(catalog_data, 3)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    context = {'data': contacts,
               'category': category}
    return render(request, 'homepage/catalog.html', context)
