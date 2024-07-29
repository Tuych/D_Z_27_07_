from django.shortcuts import render, get_object_or_404
from .models import Notebook


def home(request):
    data = Notebook.objects.all()
    context = {
        'data': data
    }
    return render(request, 'info/home.html', context)


def detail(request, detail_id):
    info = get_object_or_404(Notebook, pk=detail_id)
    context = {
        'info': info
    }
    return render(request, 'info/detail.html', context)
