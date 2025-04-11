# main/models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.venue} on {self.date.strftime('%Y-%m-%d')}"
