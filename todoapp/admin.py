from django.contrib import admin
from .models import TodoApp

# Register your models here.
class TodoAppList(admin.ModelAdmin):
    list_display = ("id", "task_name", "task_created")

admin.site.register(TodoApp, TodoAppList)