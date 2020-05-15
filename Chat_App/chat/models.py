from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_pic = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    reciever = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='reciever')
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.sender.user.username
        # return f"{self.sender.user.username} to {self.reciever.user.username}"
    