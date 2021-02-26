from django.db import models


class Students(models.Model):
    e_no = models.IntegerField()
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

