from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default_profile.png' )
    friends = models.ManyToManyField('Friend', related_name='friends', blank=True, null=True, )

    def __str__(self):
        return str(self.name)
    

class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profile.name)