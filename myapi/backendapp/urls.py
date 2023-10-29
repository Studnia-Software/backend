from django.urls import path
from backendapp.views import ping, create_order, store, get_farms, get_farm_posts, get_user, get_farms_user_area, get_users, fetch_farm_orders

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('store/', store, name='store'),
    path('get-farms/', get_farms, name='get_farms'),
    path('get-farm-posts/<int:farm_id>', get_farm_posts, name='get_farm_posts'),
    path('get-user/<int:user_id>', get_user, name='get_user'),
    path('get-farms-user-area/<int:user_id>', get_farms_user_area, name='get_farms_user_area'),
    path('create-order/', create_order, name='create_order'),
    path('fetch-farm-orders/<int:id>/', fetch_farm_orders, name='fetch_farm_orders'),
    path('get-users/', get_users, name='get_users')
]