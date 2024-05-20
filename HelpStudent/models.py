

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField()

    class Meta:
        app_label = 'HelpStudent'

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class StageOffer(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    
class Logement(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200) 
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
   
    
    def __str__(self):
        return self.nom
   



class Transport(models.Model):
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    vehicle = models.CharField(max_length=100)
    description = models.TextField()

class Publication(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
