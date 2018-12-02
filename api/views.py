from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from .serializers import UserCreateSerializer, ItemListSerializer, BiddingListSerializer, CategorySerializer, ItemDetailSerializer, FullUserSerializer, BiddingCreateSerializer, UpdateFullUserSerializer
from .models import Item, Bidding, Category, User
from rest_framework.views import APIView
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
	serializer_class = ItemListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'


class ProfileAPIView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = FullUserSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'


class BiddingCreateView(CreateAPIView):
	serializer_class = BiddingCreateSerializer
	permission_classes = [IsAuthenticated]
	def perform_create(self, serializer):
		serializer.save(user=self.request.user, item=Item.objects.get(id=self.kwargs['object_id']))
		new_item = Item.objects.get(id=self.kwargs['object_id'])
		new_item.highest_bid=serializer.data["amount"]
		new_item.save()
		print(new_item.highest_bid)

class ProfileUpdateView(APIView):
	serializer_class = UpdateFullUserSerializer
	
	def put(self, request, *args, **kwargs):
		serializer.save(user=self.request.user, item=Item.objects.get(id=self.kwargs['object_id']))


