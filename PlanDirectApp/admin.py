from django.contrib import admin
from .models import Entry, toDo
# Register your models here.

admin.site.register(Entry)
admin.site.register(toDo)