from django.db import models


class Notebook(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()

    def __str__(self):
        return self.title

