from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your models here.
class Entry(models.Model):
    text = models.CharField(max_length=5000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField()

    def __str__(self):
        return f'{self.created_by}; {self.created_date}; {self.text}'

class toDo(models.Model):
    task = models.CharField('Task', max_length=100)
    date_added = models.DateTimeField('Date added',auto_now_add=True)
    completed = models.BooleanField('Done?', default=False)
    
    def __str__(self):
        return self.task