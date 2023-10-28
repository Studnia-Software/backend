from django.urls import path
from backendapp.views import ping, store_post  # Import the 'home' view

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('store/', store_post)  # This pattern matches the root URL ('/')
    # ...other paths if you have any
]