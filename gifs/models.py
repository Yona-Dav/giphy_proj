from django.db import models

# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField('Gif')

    def __str__(self):
        return self.name

