from rest_framework import generics
from .serializers import OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()
