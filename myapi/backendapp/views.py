from django.shortcuts import render
from django.http import JsonResponse

def ping(request):
    return JsonResponse({'message': "dziala w chuj"})


def products(request):
    return JsonResponse(
        {
        'status': 200,
        'products': [
            {'id': 1, 'name': 'gowno', 'description': 'chuj'},
            {'id': 2, 'name': 'kupa', 'description': 'chuj'},
            {'id': 3, 'name': 'dupa', 'description': 'chuj'}
        ]
    }
    )

    