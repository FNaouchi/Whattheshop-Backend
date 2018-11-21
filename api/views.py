from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, ItemListSerializer, BiddingListSerializer, CategorySerializer
from .models import Item, Bidding, Category

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import OrderingFilter, SearchFilter


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ItemListAPIView(ListAPIView):

	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class BiddingListAPIView(ListAPIView):

	queryset = Bidding.objects.all()
	serializer_class = BiddingListSerializer