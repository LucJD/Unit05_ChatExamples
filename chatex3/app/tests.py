from django.test import TestCase

# Create your tests here.

from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from app import models

# Create your tests here.


class Test_Channel(TestCase):
    def test_can_create_message(self):
        channel1 = models.create_channel("Channel name")
        self.assertEquals(channel1.name, "Channel name")


class Test_User(TestCase):
    def test_can_create_user(self):
        user1 = models.create_user("User name")
        self.assertEquals(user1.name, "User name")

    def test_can_create_user_with_channel(self):
        channel1 = models.create_channel("Channel name")
        channel2 = models.create_channel("Channel Name 2")

        # ====EXTRA TESTS====#
        # --- showing how many-to-many relationships need to be established
        # also, showing methods to pass in an arbitrary number of channels for
        # a many to many relationship

        # TEST ONE -- Test how to add channels to a user
        user_with_channel_test = models.create_user_with_channel(
            "User name 2", channel1
        )
        self.assertEquals(user_with_channel_test.channels.get(id=channel1.id), channel1)
        # TEST TWO -- Test how to add arbitrary argument
        # test using arbitrary number of channels
        channels = models.Channel.objects.all().filter(name__startswith="Channel")
        user_with_many_channels = models.create_user_with_many_channels(
            "User Name 3",
            models.Channel.objects.all().filter(name__startswith="Channel"),
        )


class Test_Message(TestCase):
    def test_can_create_message(self):
        channel1 = models.create_channel("Channel name")
        user1 = models.create_user("User name")

        # message1, connected to user1 and channel1

        message1 = models.create_message(user1, channel1, "Hey bro whats up")
        self.assertEquals(message1.user, user1)
        self.assertEquals(message1.channel, channel1)

        # check that messages can be accessed via channels and users
        self.assertEquals(1, len(channel1.message_set.all()))
        self.assertEquals(1, len(user1.message_set.all()))
        self.assertEquals(
            "Hey bro whats up", channel1.message_set.get(text="Hey bro whats up").text
        )
        self.assertEquals(
            "Hey bro whats up", user1.message_set.get(text="Hey bro whats up").text
        )

    def test_messages_for(self):
        channel1 = models.create_channel("Channel name")
        user1 = models.create_user("User name")
        message1 = models.create_message(user1, channel1, "Hey bro whats up")
        message2 = models.create_message(user1, channel1, "hello")

        self.assertEquals(2, len(models.messages_for(channel1)))

    def test_active_users(self):
        channel1 = models.create_channel("Channel name")
        user1 = models.create_user("User name")
        message1 = models.create_message(user1, channel1, "Hey bro whats up")
        message2 = models.create_message(user1, channel1, "hello")

        self.assertEquals(1, len(models.active_users(channel1)))

    def test_lurkers(self):
        channel1 = models.create_channel("Channel name")
        user1 = models.create_user("User name")
        user2 = models.create_user("User name 2")
        lurker = models.create_user("Lurker")

        # lurker is not associated with these messages
        message1 = models.create_message(user1, channel1, "Hey bro whats up")
        message2 = models.create_message(user2, channel1, "hello")

        users = models.lurkers(channel1)
        self.assertEquals(1, len(users))
