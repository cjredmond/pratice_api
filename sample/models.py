from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    number = models.IntegerField()

class FreeAgent(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

class PackersPlayer(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
