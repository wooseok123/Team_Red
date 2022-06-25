from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    id = models.CharField(max_length=50)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.name