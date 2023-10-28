from django.db import models


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    role_id = models.ForeignKey(to=Role, on_delete=models.CASCADE)


class Farm(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    delivery_time = models.CharField(max_length=64)


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
    farm_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    price_id = models.ForeignKey(to=Price, on_delete=models.CASCADE)
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)

# Create your models here.
