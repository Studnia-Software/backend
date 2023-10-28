from django.core.management.base import BaseCommand
from backendapp import models
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        cities_areas = {
            "Poznan": [
                "Lazarz",
                "Grunwald",
                "Stare Miasto",
                "Jezyce",
                "Wilda"
            ],
            "Wroclaw": [
               "Fabryczna",
                "Stare Miasto",
                "Srodmiescie",
                "Krzyki",
                "Psie Pole"
            ],
            "Krakow": [
                "Stare Miasto",
                "Nowy Swiat",
                "Wawel",
                "Nowa Huta",
                "Kazimierz"
            ],
            "Lodz": [
                "Srodmiescie",
                "Baluty",
                "Widzew",
                "Polesie",
                "Gorna"
            ],
            "Warszawa": [
                "Srodmiescie",
                "Praga",
                "Bemowo",
                "Mokotow",
                "Ochota",
            ],
            "Katowice": [
                "Srodmiescie",
                "Zawodzie",
                "Osiedle Paderewskiego-Muchowiec",
                "Zaleska Halda",
                "Ligota-Panewniki"
            ]
        }

        producer = models.Role(name='producer')
        consumer = models.Role(name='consumer')
        producer.save()
        consumer.save()

        user_roles = [producer, consumer]

        cities_areas_objs = {}

        for city in cities_areas:
            new_city = models.City(name=city)
            new_city.save()

            for area in cities_areas[city]:
                new_area = models.Area(city_id=new_city, name=area)
                new_area.save()

                if city in cities_areas_objs.keys():
                    cities_areas_objs[city].append(new_area)
                else:
                    cities_areas_objs[city] = [new_area]

        for city in cities_areas_objs:
            for area in cities_areas_objs[city]:
                for _ in range(15):
                    new_user = models.User(role_id=user_roles[1], area_id=area)
                    new_user.save()

                for i in range(3):
                    new_user = models.User(role_id=user_roles[0], area_id=area)
                    new_user.save()

                    new_farm = models.Farm(user_id=new_user, name=f"Kurewska Farma {i}", delivery_days="Mon, Fri", delivery_time=f"09:00-1{i}:00")
                    new_farm.save()

                    new_area_farms_relation = models.AreaFarmsRelation(area_id=area, farms_id=new_farm)
                    new_area_farms_relation.save()

                    prev_areas = []
                    for _ in range(random.randrange(1, 5)):
                        random_area = cities_areas_objs[city][random.randrange(0, 5)]
                        while random_area in prev_areas:
                            random_area = cities_areas_objs[city][random.randrange(0, 5)]

                        prev_areas.append(random_area)
                        new_area_farms_relation = models.AreaFarmsRelation(area_id=random_area, farms_id=new_farm)
                        new_area_farms_relation.save()

                    for j in range(5):
                        new_product = models.Product(name=f"Gówno {i}", description="Gówno z krowy jeszcze ciepłe")
                        new_product.save()
                        new_price = models.Price(price_per_unit=50 * i, quantity=1 + i, per_kg=bool(i % 2))
                        new_price.save()
                        new_post = models.Post(farm_id=new_farm, price_id=new_price, product_id=new_product, title=f"Dupa {i}")
                        new_post.save()

        print('Database generated')
