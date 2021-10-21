from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
import pytz

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
def new_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        toDo.objects.create(
            new_task=task
        )


def get_tasks(request):
    task_objects = toDo.objects.all()
    tasks = []
    for task_object in task_objects:
        task = {
            'id' : task_object.id,
            'task' : task_object.task,
            'details' : task_object.details,
            'start' : task_object.date_added,
            'completed' : task_object.completed
        }
        tasks.append(task)
    data = {
        'tasks' : tasks
    }
    return JsonResponse(data)


def covert_localtime(utctime):
    fmt = '%Y-%M-%D %T'
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(fmt)