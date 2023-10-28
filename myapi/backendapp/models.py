from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)


class Price(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    quantity = models.IntegerField()
    weight = models.FloatField()
    per_kg = models.BooleanField()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=400)


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    city_id = models.ForeignKey(to=City, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(to=Role, on_delete=models.CASCADE)
    area_id = models.ForeignKey(to=Area, on_delete=models.CASCADE)


class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    delivery_days = models.CharField(max_length=64)
    delivery_time = models.CharField(max_length=64)


class AreaFarmsRelation(models.Model):
    id = models.AutoField(primary_key=True)
    area_id = models.ForeignKey(to=Area, on_delete=models.CASCADE)
    farms_id = models.ForeignKey(to=Farm, on_delete=models.CASCADE)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    farm_id = models.ForeignKey(to=Farm, on_delete=models.CASCADE)
    price_id = models.ForeignKey(to=Price, on_delete=models.CASCADE)
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
# Create your models here.

