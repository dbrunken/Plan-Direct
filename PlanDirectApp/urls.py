from django.urls import path
from . import views

app_name = 'PlanDirectApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('new_task/', views.new_task, name='new_task'),
    path('get_tasks/', views.get_tasks, name='get_tasks')
]