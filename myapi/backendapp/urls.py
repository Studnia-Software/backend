from django.urls import path
from backendapp.views import ping, store_post, get_farms, get_farm_posts, get_user, get_farms_user_area

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('store/', store_post),
    path('get-farms/', get_farms, name='get_farms'),
    path('get-farm-posts/<int:farm_id>', get_farm_posts, name='get_farm_posts'),
    path('get-user/<int:user_id>', get_user, name='get_user'),
    path('get-farms-user-area/<int:user_id>', get_farms_user_area, name='get_farms_user_area')
]