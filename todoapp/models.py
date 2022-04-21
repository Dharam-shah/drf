from django.db import models

# Create your models here.
class TodoApp(models.Model):
    task_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default="download.png")
    task_created = models.DateTimeField(auto_now_add=True)
    dead_line = models.DateTimeField()
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name