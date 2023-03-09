from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# INTERPRETATION 2
# create m2m field in user rather than channel, let 2-way relationship come by default

# In this example, we are letting the two-way relationship come by default
# we are also not using related_name, and showcasing the differences
class Channel(models.Model):
    name = models.TextField()
    # channel_users, a list will be made via many-to-many on User class


# look at comments for Channel
class User(models.Model):
    name = models.TextField()
    channels = models.ManyToManyField(Channel, related_name="channel_users")


# one user can have many messages, messages can only have one user -> one to many
# - use foreign key with user being key
# one channel can have many messages, messages can only have one channel -> one to many
# - use foreign key with channel being key
class Message(models.Model):
    user = models.ForeignKey(
        User, related_name="messages_from_user", on_delete=models.CASCADE
    )  # message_set
    channel = models.ForeignKey(
        Channel, related_name="messages_on_channel", on_delete=models.CASCADE
    )
    text = models.TextField()


def create_channel(name):
    channel = Channel(name=name)
    channel.save()
    return channel


def create_user(name):
    user = User(name=name)
    user.save()
    return user


# Create message
# on creation of message, we can add channels to user
# channel will update list of channel_users on user.save(), we do not have to automatically
# .add(arg) calls .save(), so we don't have to


def create_message(user, channel, text):
    message = Message(user=user, channel=channel, text=text)
    user.channels.add(channel)
    message.save()
    return message


def messages_for(channel):
    return channel.messages_on_channel.all()


def active_users(channel):
    return channel.channel_users.all()


def lurkers(channel):
    return User.objects.all().exclude(id__in=channel.channel_users.all())
