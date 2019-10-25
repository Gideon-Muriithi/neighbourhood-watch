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

