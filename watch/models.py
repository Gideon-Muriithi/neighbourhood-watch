from django.db import models
from django.contrib.auth.models import User

class Neighbourhood(models.Model):
    neighbourhood = models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()



class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile_pics/')
    neighbourhood_name = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    neighbourhood_description = models.TextField()

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(blank=True, max_length=30)
    email = models.EmailField(max_length=70, blank=True)
    business_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    business_hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='biz', null=True)