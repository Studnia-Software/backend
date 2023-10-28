from django.test import TestCase
from .models import Post

class PostTestCase(TestCase):
    def test_post_store(self):
        # Simulate a POST request to your endpoint
        response = self.client.post('/api/store/', {
            'title': 'tytul1',
            'name': 'nazwa produktu 1',
            'description': 'opis produktu asdalaldasljdasljkdalsjkdalsjkdaslkdjlkas',
            'farm_id': 1,
            'amount': 500,
            'quantity': 1,
            'weight': 30,
            'per_kg': 0
        })

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Optionally, check if the value was stored in the database
        self.assertEqual(Post.objects.count(), 1)
