from django.db import models
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=25, default="none")
    img_url = models.CharField(max_length=256)
    info = models.CharField(max_length=512)
    story = models.CharField(max_length=1024)
    rating = models.FloatField()

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'title':self.title})
