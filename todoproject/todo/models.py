from django.db import models

# Create your models here.

CHOICE=(('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    memo=models.TextField()
    priority=models.CharField(
        choices=CHOICE,
        max_length=50
        ) 
    duedate=models.DateField()

    def __str__(self):
        return self.title
    