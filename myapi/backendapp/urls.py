from django.urls import path
from backendapp.views import ping  # Import the 'home' view

urlpatterns = [
    path('ping/', ping, name='ping'),  # This pattern matches the root URL ('/')
    # ...other paths if you have any
]