from ..models import Post, Product, Farm, Price
class PostService:

    def store(self, arr):
        title = arr['title']
        product_name = arr['product_name']
        product_description = arr['product_description'] 
        farm_id = arr['farm_id']
        amount = arr['amount']
        quantity = arr['quantity']
        weight = arr['weight']
        per_kg = arr['per_kg']

        product = Product(
            name=product_name,
            description=product_description
        )
        product.save()
        print("product saved")

        price = Price(
            amount = amount,
            quantity = quantity,
            weight = weight,
            per_kg = per_kg
        )

        price.save()
        print("price saved")


        price = Price.objects.get(id=price.id)
        product = Product.objects.get(id=product.id)
        farm = Farm.objects.get(id=farm_id)


        post = Post(
            title=title,
            product_id=product,
            farm_id=farm,
            price_id=price
        )

        post.save()
        print("post saved")

        