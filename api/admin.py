from django.contrib import admin
from .models import Item, Profile, Bidding, ItemType, Category

admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(Bidding)
admin.site.register(Profile)
admin.site.register(Category)