from django.test import TestCase

from users.models import SmartGymUser
from django.contrib.auth.models import User

class SmartGymUserCreationTest(TestCase):
    def test_smartgymuser_creation(self):
        user = User(username="TestUser")
        self.assertNotEqual(user.smartgymuser, None)
    
