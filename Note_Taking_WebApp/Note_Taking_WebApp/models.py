
from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"