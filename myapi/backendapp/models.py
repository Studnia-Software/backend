from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=16)


class Price(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.FloatField()
    quantity = models.IntegerField()
    weight = models.FloatField()
    per_kg = models.BooleanField()


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    price_id = models.ForeignKey(to=Price, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)






# Create your models here.
