from django.db import models


class Film(models.Model):
    nazev = models.CharField(max_length=100)
    rok = models.IntegerField()
    zanr = models.CharField(max_length=50)
    reziser = models.CharField(max_length=100)
    popisek = models.TextField()

    def __str__(self):
        return self.nazev
