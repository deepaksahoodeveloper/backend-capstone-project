# Importing necessary modules
from django.test import TestCase
from littlelemon_api.models import Menu  # Importing the Menu model from your app

# Test class for Menu model
class MenuTest(TestCase):
    # Test method to add a new instance of the Menu model
    def test_add_menu_item(self):
        # Creating a new instance of the Menu model
        menu_item = Menu.objects.create(name="Ice Cream", price=80, inventory=100)
        
        # Asserting the string representation of the newly added object
        self.assertEqual(str(menu_item), "Ice Cream : 80")
