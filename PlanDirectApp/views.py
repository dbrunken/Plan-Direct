from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from datetime import datetime
import pytz
import json

from .models import Entry, toDo

# Create your views here.
def index(request):
    entries = Entry.objects.all()
    tasks = toDo.objects.all()
    context = {
        'entries' : entries,
        'tasks' : tasks
    }
    return render(request, 'PlanDirectApp/index.html', context)

@login_required
def new_entry(request):
    if request.method == 'POST':
        entry = request.POST.get('entry')
        Entry.objects.create(
            text=entry,
            created_date=timezone.now(),
            created_by=request.user
        )
        return redirect('PlanDirectApp:index')

@login_required
def history(request):
    entry_objects = Entry.objects.all()
    entries = []
    for entry_object in entry_objects:
        entry = {
            'id':entry_object.id,
            'entry':entry_object.text,
            'created_date':entry_object.created_date
        }
        entries.append(entry)
    data = {
        'entries':entries
    }
    return JsonResponse(data)

@login_required
def new_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # task = request.POST.get('task')

        toDo.objects.create(
            task=data.get('task'),
            details=data.get('details'),
            start=data.get('start'),
            color=data.get('color')
        )
    return HttpResponse('Added Task')


def get_tasks(request):
    task_objects = toDo.objects.all()
    tasks = []
    for task_object in task_objects:
        task = {
            'id' : task_object.id,
            'task' : task_object.task,
            'details' : task_object.details,
            'start' : task_object.start,
            'completed' : task_object.completed,
            'color' : task_object.color,
        }
        tasks.append(task)
    data = {
        'tasks' : tasks
    }
    return JsonResponse(data)

@login_required
def update_task(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        todo = toDo.objects.get(id=id)
        todo.details = data.get('details')
        todo.save()
        # toDo.objects.update(details=data.get('details'))
    return HttpResponse('task updated')

@login_required
def delete_task(request, id):
    task = toDo.objects.get(id=id)
    task.delete()
    return HttpResponse('task deleted')

def covert_localtime(utctime):
    fmt = '%Y-%M-%D %T'
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(fmt)