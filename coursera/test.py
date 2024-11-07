from django.test import TestCase as DjangoTestCase


class TestCase(DjangoTestCase):

    def set_user(self, user):
        self.user = user
        self.client.force_login(self.user)
