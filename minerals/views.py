from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Mineral


def index(request):
    minerals = get_list_or_404(Mineral)
    return render(request, 'minerals/index.html',
                  {'minerals': minerals})


def detail(request, name):
    if name == 'random-mineral':
        mineral = Mineral.objects.order_by('?').first()
    else:
        mineral = get_object_or_404(Mineral, name=name)
    data = model_to_dict(mineral, exclude=['id', 'image_caption',
                                           'image_filename', 'name'])
    return render(request, 'minerals/detail.html',
                  {'data': data, 'mineral': mineral})







