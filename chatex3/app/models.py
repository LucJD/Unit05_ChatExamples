from django.db import models

# Create your models here.

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


# ---In this example, we are discussing direct assignments to many-to-many
# along with a way to add arbitrary number of arguments


class Channel(models.Model):
    name = models.TextField()
    # channel_users


# look at comments for Channel
class User(models.Model):
    name = models.TextField()
    channels = models.ManyToManyField(
        Channel, related_name="channel_users", related_query_name="channel_user"
    )


# one user can have many messages, messages can only have one user -> one to many
# - use foreign key with user being key
# one channel can have many messages, messages can only have one channel -> one to many
# - use foreign key with channel being key
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # message_set
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    text = models.TextField()


def create_channel(name):
    channel = Channel(name=name)
    channel.save()
    return channel


def create_user(name):
    user = User(name=name)
    user.save()
    return user


def create_user_with_channel(name, channels):
    # user = User(name=name, channels=channels)
    # user.save()
    user = User(name=name)
    user.save()
    user.channels.add(channels)
    return user


def create_user_with_many_channels(name, channels):
    user = User(name=name)
    user.save()
    user.channels.add(*channels)
    return user


# Create message
# on creation of message, we can also save the user
# channel will update list of channel_users on user.save()
def create_message(user, channel, text):
    message = Message(user=user, channel=channel, text=text)
    user.channels.add(channel)
    user.save()
    message.save()
    return message


def messages_for(channel):
    return channel.message_set.all()


def active_users(channel):
    return channel.channel_users.all()


def lurkers(channel):
    return User.objects.all().exclude(id__in=channel.channel_users.all())
