from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.test import Client
from order.models import UserProfile, Order
from order.views import OrderCreateAPIView


class OrderTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        # create data
        self.user = UserProfile.objects.create(
            username="test_user", wallet_amount=1000
        )
        self.order = Order.objects.create(
            user=self.user, crypto_name='ABAN', crypto_volume=3,
        )

    def test_details(self):
        response = self.client.post('/order/purchase/', {'user': self.user, 'crypto_name': 'ABAN',
                                                         'crypto_volume': 3})
        self.assertEqual(response.status_code, 201)


