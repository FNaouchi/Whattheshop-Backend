from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item, Bidding, ItemType, Category, Profile

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email',
                  'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']


class FullUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                   "profile"]


class BiddingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Bidding
        fields = ["amount", "user"]


class ItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ["id","name","description","end_date", "logo"]

class ItemListSerializer(serializers.ModelSerializer):
    biddings = BiddingSerializer(many=True)

    class Meta:
        model = Item
        fields = ["id","name","description", "end_date", "logo", "biddings"]


class ItemTypeSerializer(serializers.ModelSerializer):
    items = ItemDetailSerializer(many=True)
    class Meta:
        model = ItemType
        fields = ["id","name","items"]


class BiddingListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    item = ItemListSerializer()
    class Meta:
        model = Bidding
        fields = ["user","amount","item"]


class CategorySerializer(serializers.ModelSerializer):
    item_types = ItemTypeSerializer(many=True)
    class Meta:
        model = Category
        fields = ["id","name","item_types"]
