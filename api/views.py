from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer, ItemListSerializer, BiddingListSerializer, CategorySerializer, ItemDetailSerializer, FullUserSerializer
from .models import Item, Bidding, Category, User

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

class ItemsDetailAPIView(RetrieveAPIView):
	
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'


class ProfileAPIView(RetrieveAPIView):

	queryset = User.objects.all()
	serializer_class = FullUserSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'
