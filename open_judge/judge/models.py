from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name+"- "+self.score