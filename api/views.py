from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, ItemListSerializer, BiddingListSerializer
from .models import Item, Bidding

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import OrderingFilter, SearchFilter


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ItemListAPIView(ListAPIView):

	queryset = Item.objects.all()
	serializer_class = ItemListSerializer

class BiddingListAPIView(ListAPIView):

	queryset = Bidding.objects.all()
	serializer_class = BiddingListSerializer