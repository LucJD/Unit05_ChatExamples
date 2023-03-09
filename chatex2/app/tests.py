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
        channel1 = models.create_channel("Channel name")
        self.assertEquals(user1.name, "User name")


class Test_Message(TestCase):
    def test_can_create_message(self):
        channel1 = models.create_channel("Channel name")
        user1 = models.create_user("User name")

        # message1, connected to user1 and channel1

        message1 = models.create_message(user1, channel1, "Hey bro whats up")
        self.assertEquals(message1.user, user1)
        self.assertEquals(message1.channel, channel1)

        # check that messages can be accessed via channels and users
        self.assertEquals(1, len(channel1.messages_on_channel.all()))
        self.assertEquals(1, len(user1.messages_from_user.all()))
        self.assertEquals(
            "Hey bro whats up",
            channel1.messages_on_channel.get(text="Hey bro whats up").text,
        )
        self.assertEquals(
            "Hey bro whats up",
            user1.messages_from_user.get(text="Hey bro whats up").text,
        )

    def test_messages_for(self):
        channel1 = models.create_channel("Channel name")
        user1 = models.create_user("User name")
        message1 = models.create_message(user1, channel1, "Hey bro whats up")
        message2 = models.create_message(user1, channel1, "hello")

        self.assertEquals(2, len(models.messages_for(channel1)))

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
