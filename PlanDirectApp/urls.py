from django.urls import path
from . import views

app_name = 'PlanDirectApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('new_task/', views.new_task, name='new_task'),
    path('get_tasks/', views.get_tasks, name='get_tasks'),
    path('history/', views.history, name='history'),
    path('get_history/', views.get_history, name='get_history'),
    path('update_task/<int:id>', views.update_task, name='update_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
]