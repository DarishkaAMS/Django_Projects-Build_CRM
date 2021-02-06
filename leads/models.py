from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_picture = models.ImageField(blank=True, null=True)
    special_fields = models.FileField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def post_user_created_signal(sender, instance, created, **kwargs):
    print(sender)
    print(instance)
    print(created)


post_save.connect(post_user_created_signal, sender=User)