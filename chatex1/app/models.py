from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# INTERPRETATION 1
# manytomanyfields are already a 2 way relationship
# so there isn't explicit need to have a manytomany field on both the Channel and User class
# but you can, and its on the readme
# -------------------------------------------------------
# one user can have many channels
# one channel can have many users
# manytomany field
# doing "User" before User is created will be sure
# that User class will take its place


# ---In this example, we are using a manytomany field relationship and manually creating the two-way relationship
# we are also using _set field


class Channel(models.Model):
    name = models.TextField()
    users = models.ManyToManyField('User')
    #message_set


# look at comments for Channel
class User(models.Model):
    name = models.TextField()
    channels = models.ManyToManyField(
        Channel
    )
    #message_set


# one user can have many messages, messages can only have one user -> one to many
# - use foreign key with user being key
# one channel can have many messages, messages can only have one channel -> one to many
# - use foreign key with channel being key
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # message_set
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    text = models.TextField()
#message_set

def create_channel(name):
    channel = Channel(name=name)
    channel.save()
    return channel


def create_user(name):
    user = User(name=name)
    user.save()
    return user



# Create message
# on creation of message, we also add channel to user and user to channel
# .add(arg) will call .save(), so we don't need to
def create_message(user, channel, text):
    message = Message(user=user, channel=channel, text=text)
    user.channels.add(channel)
    channel.users.add(user)
    message.save()
    return message


def messages_for(channel):
    return channel.message_set.all()


def active_users(channel):
    return channel.users.all()


def lurkers(channel):
    return User.objects.all().exclude(id__in=channel.users.all())
