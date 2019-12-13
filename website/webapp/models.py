from django.db import models

# Create your models here.
class employees(models.Model):
    name=models.CharField(max_length=10)
    unique_id=models.CharField(max_length=10)
    salary = models.CharField(max_length=10)
    type = models.IntegerField()


    def __str__(self):
        return self.name



