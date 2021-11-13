from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class JobAdd(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    hamount = models.IntegerField(default=1,
                                  validators=[
                                     MaxValueValidator(1000),
                                     MinValueValidator(1)
                                 ])
    companyname = models.CharField(max_length=200)
