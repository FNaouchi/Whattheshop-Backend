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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']


class BiddingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Bidding
        fields = ["amount", "user"]

    def get_user(self, obj):
        return obj.user.username

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id","name","description", "duration", "starting_price", "highest_bid" ,"end_date", "logo"]

class ProfileBiddingSerializer(serializers.ModelSerializer):
    item = ItemDetailSerializer()
    class Meta:
        model = Bidding
        fields = ["amount", "item"]

class FullUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    biddings = ProfileBiddingSerializer(many=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                   "profile", "biddings"]

class UpdateFullUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                   "profile"]

class ItemListSerializer(serializers.ModelSerializer):
    biddings = BiddingSerializer(many=True)

    class Meta:
        model = Item
        fields = ["id","name","description", "duration", "starting_price", "highest_bid" , "end_date", "logo", "biddings"]


class ItemTypeSerializer(serializers.ModelSerializer):
    items = ItemDetailSerializer(many=True)
    class Meta:
        model = ItemType
        fields = ["id","name", "logo" ,"items"]


class BiddingListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    item = ItemListSerializer()
    class Meta:
        model = Bidding
        fields = ["user","amount","item"]

    def get_user(self, obj):
        return obj.user.username

class BiddingCreateSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Bidding
        fields = ["amount","item"]

class CategorySerializer(serializers.ModelSerializer):
    item_types = ItemTypeSerializer(many=True)
    class Meta:
        model = Category
        fields = ["id","name", "logo","item_types"]
