from django.db import models

# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    id = models.CharField(max_length=12, primary_key=True)
    vote_to = models.CharField(max_length=50)

def __str__(self):
    return self.name

class survey(models.Model):
    name = models.ForeignKey(data, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

def __str__(self):
    return self.name