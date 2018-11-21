from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item, Bidding, ItemType

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


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ["name"]


class ItemListSerializer(serializers.ModelSerializer):
    item_type = ItemTypeSerializer()
    class Meta:
        model = Item
        fields = ["name","description","end_date","item_type","logo"]


class BiddingListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    item = ItemListSerializer()
    class Meta:
        model = Bidding
        fields = ["user","amount","item"]
