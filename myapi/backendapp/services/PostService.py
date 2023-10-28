from ..models import Post
from ..models import Product
from ..models import Price
class PostService:

    def store(self, arr):
        title = arr['title']
        product_name = arr['product']['name'] 
        user_id = arr['user_id']
        amount = arr['price']['amount']
        quantity = arr['price']['quantity']
        weight = arr['price']['weight']
        per_kg = arr['price']['per_kg']

        product = Product(
            name=product_name
        )

        product.save()

        price = Price(
            amount = amount,
            quantity = quantity,
            weight = weight,
            per_kg = per_kg
        )

        price.save()

        post = Post(
            title=title,
            product_id=product.id,
            user_id=user_id,
            price_id=price.id
        )

        post.save()
        