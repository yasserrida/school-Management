from django.db import models


class student(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gender = models.TextChoices('homme', 'femme')
    birthday = models.DateTimeField()
    note = models.IntegerField()
