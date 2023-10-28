from django.urls import path
from backendapp.views import ping, store_post, get_farms, get_farm_posts, get_farm

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('store/', store_post),
    path('get-farms/', get_farms, name='get_farms'),
    path('get-farm-posts/<int:id>', get_farm_posts, name='get_farm_posts'),
    path('get-farm/<int:id>', get_farm, name='get_farm')
]