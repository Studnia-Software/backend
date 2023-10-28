from django.core.management.base import BaseCommand
from backendapp import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        producer = models.Role(name='producer')
        consumer = models.Role(name='consumer')

        producer.save()
        consumer.save()
        user_roles = [producer, consumer]

        for _ in range(15):
            new_user = models.User(role_id=user_roles[1])
            new_user.save()

        for i in range(5):
            new_user = models.User(role_id=user_roles[0])
            new_user.save()

            new_farm = models.Farm(user_id=new_user, name=f"Kurewska Farma {i}", delivery_days="Mon, Fri", delivery_time=f"09:00-1{i}:00")
            new_farm.save()

            for j in range(5):
                new_product = models.Product(name=f"Gówno {i}", description="Gówno z krowy jeszcze ciepłe")
                new_product.save()
                new_price = models.Price(amount=50 * i, quantity=1 + i, weight=100 * i, per_kg=bool(i % 2))
                new_price.save()
                new_post = models.Post(farm_id=new_farm, price_id=new_price, product_id=new_product, title=f"Dupa {i}")
                new_post.save()

        print('Database generated')
