from django.shortcuts import render
from django.http import JsonResponse
import json
from .services.PostService import PostService
from django.views.decorators.csrf import csrf_exempt
from .models import Farm, Post, Price, AreaFarmsRelation, User, OrderInfo, Order, Role
from .serializers import serialize_farm, serialize_order

@csrf_exempt
def ping(request):
    return JsonResponse({'message': "dziala w chuj"})


@csrf_exempt
def store_post(request):
    if request.method == 'POST':
        try:
            # Check if the Content-Type is application/json
            if 'application/json' in request.content_type:
                # Parse the JSON data
                json_data = json.loads(request.body.decode('utf-8'))
                
                # Now, json_data is a Python dictionary containing your JSON data
                # You can access it like any other dictionary
                data_dict = {
                    'title': json_data.get('title'),
                    'product_name': json_data.get('product_name'),
                    'product_description': json_data.get('product_description'),
                    'farm_id': json_data.get('farm_id'),
                    'amount': json_data.get('amount'),
                    'quantity': json_data.get('quantity'),
                    'weight': json_data.get('weight'),
                    'per_kg': json_data.get('per_kg')
                    }               

                post_service = PostService()    
                post_service.store(data_dict)
                # Do something with the data
                
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
        body = request.data

        user = User.objects.get(id=body["user_id"])
        farm = Farm.objects.get(id=body["farm_id"])
        post = Post.objects.get(id=body["post_id"])
        quantity = body["quantity"]
        per_kg = body["per_kg"]

        if quantity > post.price_id.quantity:
            print("Too much")

        product = post.product_id
        total_price = post.price_id.price_per_unit * quantity

        new_order_info = OrderInfo(product_id=product, total_price=total_price, quantity=quantity, per_kg=per_kg)
        new_order_info.save()
        new_order = Order(user_id=user, farm_id=farm, order_info_id=new_order_info)
        new_order.save()

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





