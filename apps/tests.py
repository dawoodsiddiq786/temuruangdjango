from django.test import TestCase
# Create your tests here.
from rest_framework import status
from rest_framework.test import APIClient

from apps.models import User

client = APIClient()


class ProductTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(name='Tas', email='test@gmail.com', password='1234rtyu')

    def test_login_success(self):
        response = client.get(
            '/v0/user/',
            {
                'email': 'test@gmail.com',
                'password': '1234rtyu',

            }
            , format='json',
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
