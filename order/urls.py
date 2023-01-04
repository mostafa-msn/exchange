from django.urls import path


urlpatterns = [
    path('purchase/', OrderCreateAPIView.as_view()),
    ]