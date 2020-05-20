from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from movie.models import Movie

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    history = models.ManyToManyField(Movie, related_name="history", blank=True, through='ThroughModel')
    watchlist = models.ManyToManyField(Movie, related_name="watchlist", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class ThroughModel(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_viewed = models.DateTimeField(auto_now_add=True)

   # def save(self, *args, **kwargs):
   #     super().save(*args, **kwargs)

   #     img = Image.open(self.image.path)
   #     if img.height > 300 or img.width > 300:
   #         output_size = (300, 300)
   #         img.thumbnail(output_size)
   #         img.save(self.image.path)
        