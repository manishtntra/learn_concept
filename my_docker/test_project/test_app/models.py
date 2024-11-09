from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField()
    designation = models.CharField()

    def __str__(self):
        return f" My Name is {self.name} a {self.designation}"