from django.urls import path
from backendapp.views import ping, store_post, get_farms

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('store/', store_post),
    path('get-farms/', get_farms, name='get_farms'),
]