from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    context = {
        'tasks': Task.objects.order_by('id'),
        'form': TaskForm(),
    }
    return render(request, 'tasks/index.html', context)
