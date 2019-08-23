from django.db import models

# Create your models here.


class Nps(models.Model):
    name = models.CharField(primary_key=True, max_length=15)
    ex_value = models.IntegerField()
    asset_rate = models.CharField(max_length=10)
    share = models.CharField(max_length=5)
    now = models.CharField(max_length=30, default=0)
    past = models.CharField(max_length=30, default=0)
    rate = models.CharField(max_length=30, default=0)
    benefit = models.CharField(max_length=30, default=0)


class Stock(models.Model):
    name = models.ForeignKey(Nps, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    value = models.CharField(max_length=20)
