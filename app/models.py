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
    

class ChatMessage(models.Model):
    message = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_sender')
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_receiver')
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.msg_sender.name + ' to ' + self.msg_receiver.name + ' : ' + self.message[:10] + '...' )