from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone

class Neighbourhood(models.Model):
    locality = models.CharField( max_length=30, default="e.g Nairobi, Thika, Ruiru etc")
    name = models.CharField(max_length=30, default='Name')
    occupants_count = models.IntegerField(default=0, blank=True)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hoods', blank=True, default=1)
    date = models.DateTimeField(default=timezone.now)

    objects = models.Manager() 

    @classmethod
    def search_neighborhood_by_name(cls, search_term):
        neighborhoods = cls.objects.filter(name__icontains=search_term)
        return neighborhoods

    @classmethod
    def one_neighborhood(cls, id):
        neighborhood = Neighborhood.objects.filter(id=id)
        return neighborhood

    @classmethod
    def all_neighborhoods(cls):
        neighborhoods = cls.objects.all()
        return neighborhoods

    @classmethod
    def get_neighborhood_by_id(cls, id):
        neighborhood = Neighborhood.objects.filter(id=Neighborhood.id)
        return neighborhood

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile


class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile_pics/')
    neighbourhood_name = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    neighbourhood_description = models.TextField()

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    class Meta:
        ordering = ['user']


class Business(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(blank=True, max_length=30)
    email = models.EmailField(max_length=70, blank=True)
    business_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    business_hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='biz', null=True)

    @classmethod
    def search_by_name(cls, search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

    @classmethod
    def get_neighborhood_businesses(cls, neighborhood_id):
        businesses = Business.objects.filter(neighborhood_id=id)
        return businesses

    @classmethod
    def get_hood_business(cls, business_hood):
        businesses = Business.objects.filter(business_hood_pk=biz_hood)
        return businesses

    @classmethod
    def get_profile_businesses(cls, profile):
        businesses = Business.objects.filter(biz_owner__pk=profile)
        return businesses

class Join(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    hood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id