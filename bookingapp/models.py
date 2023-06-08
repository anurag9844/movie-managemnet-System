from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class MovieBooking(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie_name} {self.user_id}"
