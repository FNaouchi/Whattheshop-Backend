from django.urls import path
from .views import UserCreateAPIView, BiddingListAPIView, ItemListAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('biddings/', BiddingListAPIView.as_view(), name='biddings'),
    path('items/', ItemListAPIView.as_view(), name='items'),

]