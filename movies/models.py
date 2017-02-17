from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    geners = models.CharField(max_length=50)

class Link(models.Model):

    imdbid = models.IntegerField(max_length=200)
    tmdbid = models.IntegerField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Rating(models.Model):

    rating = models.FloatField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
