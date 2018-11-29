from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import DurationField
from datetime import timedelta
class Category(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='event_logos', null=True, blank=True)
    def __str__(self):
        return self.name

class ItemType(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, related_name='item_types', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='event_logos', null=True, blank=True)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    end_date = models.DateTimeField()
    duration = models.DurationField(default=timedelta())
    starting_price = models.DecimalField(max_digits=20, decimal_places=3)
    item_type = models.ForeignKey(ItemType, related_name='items', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='event_logos', null=True, blank=True)

    def __str__(self):
        return self.name

class Bidding(models.Model):
    user = models.ForeignKey(User,  related_name='biddings', default=1, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    item = models.ForeignKey(Item, related_name='biddings', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item.name

class Profile(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='event_logos', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
