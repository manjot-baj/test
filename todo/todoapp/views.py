from django.shortcuts import render, redirect

from django.views.decorators.http import require_POST

# Create your views here.
from .models import todo
from .forms import todoforms


def index(request):
    todolist = todo.objects.order_by('id')
    form = todoforms()
    context = {'todolist': todolist, 'form': form}
    return render(request, 'todoapp/index.html', context)


@require_POST
def addtodo(request):
    form = todoforms(request.POST)
    # print(text=request.POST['text'])
    if form.is_valid():
        newtodo = todo(text=form.cleaned_data['text'])
        newtodo.save()
    return redirect('index')


def completetodo(request, todo_id):
    todoc = todo.objects.get(pk=todo_id)
    todoc.complete = True
    todoc.save()
    return redirect('index')


def deletecompletedtodo(request):
    todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deletealltodo(request):
    todo.objects.all().delete()
    return redirect('index')
