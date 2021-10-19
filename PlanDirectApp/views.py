from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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