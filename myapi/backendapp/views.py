from django.shortcuts import render
from django.http import JsonResponse

def ping(request):
    return JsonResponse({'message': "dziala w chuj"})


def store_post(request):
    if request.method == 'POST':
        try:
            # Check if the Content-Type is application/json
            if 'application/json' in request.content_type:
                # Parse the JSON data
                json_data = json.loads(request.body.decode('utf-8'))
                
                # Now, json_data is a Python dictionary containing your JSON data
                # You can access it like any other dictionary
                title = json_data.get('title')
                product = json_data.get('product')
                user_id = json_data.get('user_id')
                price = json_data.get('price')

                
                # Do something with the data
                
                return JsonResponse({'message': 'Success'})
            else:
                return JsonResponse({'error': 'Invalid Content-Type'}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid Request Method'}, status=405)






    