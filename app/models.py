from django.db import models

# Create your models here.
import app


class State(models.Model):
    abbreviation = models.CharField(max_length=2)
    name = models.CharField(max_length=100, unique=True, null=True)



    def __unicode__(self):
        return self.name

class StateCapital(models.Model):
    name = models.CharField(max_length=100)
    state = models.OneToOneField("app.State")
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    population = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=False)

    county = models.CharField(max_length=100, null=True)
    state = models.ForeignKey("app.State", null=True, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __unicode__(self):
        return self.name

