from django.shortcuts import render
from django.http import JsonResponse
import json
from .services.PostService import PostService
from django.views.decorators.csrf import csrf_exempt
from .models import Farm, Post, Price, AreaFarmsRelation, User
from .serializers import serialize_farm

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
                "amount": price.amount,
                "quantity": price.quantity,
                "weight": price.weight,
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

