from django.test import TestCase
from .models import Item

# Create your tests here.
class TestItem(TestCase):
    
    def test_done_default_value_is_False(self):
        """
        Ensure the value of 'done' is set to False when creating an item
        """
        item = Item(name = "A test item")
        self.assertEqual(item.name, "A test item")
        self.assertFalse(item.done)
        
    def test_done_value_can_be_set_to_True(self):
        """
        Ensure the value of 'done' is True when set to True when creating an item
        """
        item = Item(name = "A test item", done = True)
        self.assertEqual(item.name, "A test item")
        self.assertTrue(item.done)
        
    def test_object_name_is_equal_to_item_name(self):
        """
        Ensure the string value of the object is equal to the item name
        """
        item = Item(name = "A test item")
        self.assertEqual(str(item), "A test item")
