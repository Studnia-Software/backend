from django.shortcuts import render
from django.http import JsonResponse
import json
from .services.PostService import PostService
from django.views.decorators.csrf import csrf_exempt
from .models import Farm, Post, Price, AreaFarmsRelation, Product, User, OrderProduct, Order, Role
from .serializers import serialize_farm, serialize_order

@csrf_exempt
def ping(request):
    return JsonResponse({'message': "dziala w chuj"})


@csrf_exempt
def store(request):
    if request.method == 'POST':
        try:
            if 'application/json' in request.content_type:
                json_data = json.loads(request.body.decode('utf-8'))
                user = User.objects.get(id=json_data.get("user_id"))
                title = json_data.get("title")

                product_name = json_data.get("product_name")
                product_description = json_data.get("product_description")

                product = Product(name=product_name, description=product_description)
                product.save()

                amount = json_data.get("amount")
                quantity = json_data.get("quantity")
                per_kg = json_data.get("per_kg")

                price = Price(amount=amount, quantity=quantity, per_kg=per_kg)
                price.save()

                farm = Farm.objects.get(user_id=user)

                post = Post(farm_id=farm, price_id=price, product_id=product, title=title)
                post.save()



                
                return JsonResponse({'message': 'Success'}, status=201)
            else:
                return JsonResponse({'error': 'Invalid Content-Type'}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid Request Method'}, status=405)


@csrf_exempt
def get_farms(request):
    if request.method == 'GET':
        farms = Farm.objects.all()
        data = [serialize_farm(farm) for farm in farms]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'message': 'GET method required.'})


@csrf_exempt
def get_user(request, user_id: int):
    if request.method == "GET":
        user = User.objects.get(id=user_id)
        return JsonResponse({"id": user.id, "role": user.role_id.name, "area": user.area_id.name})
    else:
        return JsonResponse({'message': 'GET method required.'})


@csrf_exempt
def get_farms_user_area(request, user_id: int):
    if request.method == "GET":
        user = User.objects.get(id=user_id)
        area_farms_relations = AreaFarmsRelation.objects.filter(area_id=user.area_id)

        farms = [farm_relation.farms_id for farm_relation in area_farms_relations]
        data = [serialize_farm(farm) for farm in farms]

        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'message': 'GET method required.'})


@csrf_exempt
def get_farm_posts(request, farm_id: int):
    if request.method == 'GET':
        farm = Farm.objects.get(id=farm_id)
        posts = Post.objects.filter(farm_id=farm)

        farm_data = {
            "id": farm.id,
            "user_id": farm.user_id.id,
            "name": farm.name,
            "delivery_days": farm.delivery_days,
            "delivery_time": farm.delivery_time,
            "posts": []
        }

        for post in posts:
            price = post.price_id
            product = post.product_id

            price_dict = {
                "price_per_unit": price.price_per_unit,
                "quantity": price.quantity,
                "per_kg": price.per_kg,
            }

            product_dict = {
                "name": product.name,
                "description": product.description,
            }

            post_data = {
                "price": price_dict,
                "product": product_dict,
                "title": post.title
            }

            farm_data["posts"].append(post_data)

        return JsonResponse(farm_data, safe=False)
    else:
        return JsonResponse({'message': 'GET method required.'})


@csrf_exempt
def create_order(request):
    if request.method == "POST":
        json_data = request.body.decode('utf-8')
        user = User.objects.get(id=json_data.get("user_id"))
        farm = Farm.objects.get(id=json_data.get("farm_id"))
        posts = json_data.get("posts")

        new_order = Order(user_id=user, farm_id=farm, total_price=0)
        new_order.save()

        for post_json in posts:
            post = Post.objects.get(id=post_json.get("id"))
            product = post.product_id
            price = post.price_id
            quantity = post_json.get("quantity")

            order_product = OrderProduct(product_id=product, price=price.price_per_unit, quantity=quantity, per_kg=price.per_kg, order_id=new_order)
            order_product.save()

            new_order.total_price += price.price_per_unit * quantity

        return JsonResponse({'status': 200, 'message': 'Created new order'})
    else:
        return JsonResponse({'message': 'POST method required'})


def fetch_farm_orders(request, farm_id: int):
    if request.method == "GET":
        data = Order.objects.filter(farm_id=farm_id)
        orders = [serialize_order(order) for order in data]

        return JsonResponse(orders, safe=False)
    else:
        return JsonResponse({'message': 'GET method required'})


@csrf_exempt
def get_users(request):
    if request.method == "GET":
        return JsonResponse([{'id': user.id, 'role_id': user.role_id.id, 'location': {'city': user.area_id.city_id.name, 'area': user.area_id.name}} for user in User.objects.all()], safe=False)
    else:
        return JsonResponse({'message': 'GET method required'})





