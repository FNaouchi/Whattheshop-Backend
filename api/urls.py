from django.urls import path
from .views import UserCreateAPIView, BiddingListAPIView, ItemListAPIView, ItemsDetailAPIView, ProfileAPIView, ProfileUpdateView, BiddingCreateView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('biddings/', BiddingListAPIView.as_view(), name='biddings'),
    path('items/', ItemListAPIView.as_view(), name='items'),
    path('items/<int:object_id>/', ItemsDetailAPIView.as_view(), name='detail'),
    path('profile/<int:object_id>/', ProfileAPIView.as_view(), name='profile'),
    path('profile/<int:object_id>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('items/<int:object_id>/bid/', BiddingCreateView.as_view(), name='bid'),
]