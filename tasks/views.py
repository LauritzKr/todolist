from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    context = {
        'tasks': Task.objects.order_by('id'),
        'form': TaskForm(),
    }
    return render(request, 'tasks/index.html', context)


def add_task(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        new_task = Task(text=request.POST['text'])
        new_task.save()

    return redirect('index')


def cmpl_task(request, task_id):
    completed_task = Task.objects.get(id=task_id)
    completed_task.complete = True
    completed_task.save()

    return redirect('index')


def del_cmpl(request):
    Task.objects.filter(complete__exact=True).delete()

    return redirect('index')


def del_all(request):
    Task.objects.all().delete()

    return redirect('index')
