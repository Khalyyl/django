from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    # fields for the movie table
    name = models.CharField(max_length=300)
    imdb = models.URLField(max_length = 200)
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)
    description = models.CharField(max_length=1000, null=True, default=None)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
