from django.urls import path
from .views import OrderCreateAPIView


urlpatterns = [
    path('purchase/', OrderCreateAPIView.as_view()),
    ]