from django.shortcuts import render
from django.http import JsonResponse
import json
from .services.PostService import PostService
from django.views.decorators.csrf import csrf_exempt
from .models import Farm, Post, Price


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
        data = [{'id': farm.id, 'name': farm.name, 'delivery_days': farm.delivery_days, 'delivery_time': farm.delivery_time} for farm in farms]
        
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'message': 'POST method required.'})


@csrf_exempt
def get_farm_posts(request, id):
    farm = Farm.objects.get(id=id)
    posts = Post.objects.filter(farm_id=farm)

    data = []

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

        post_data = [{
            "price": price_dict,
            "product": product_dict,
            "title": post.title
        }]

        data.append(post_data)

    return JsonResponse(data, safe=False)
