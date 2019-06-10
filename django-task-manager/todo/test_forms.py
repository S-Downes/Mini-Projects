from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestToDoItemForm(TestCase):
    
    def test_can_create_an_item_with_only_a_name(self):
        """
        Ensure that forms can be created with just a name (and not setting the 'done' field to True)
        """
        form = ItemForm( {"name": "Test Item Form"} )
        self.assertTrue(form.is_valid())
        
    def test_cannot_create_an_item_without_a_name(self):
        """
        Ensure that forms cannot be created without a name being added to the item
        """
        form = ItemForm( {"name": ""} )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u"This field is required."])
        
    
        
        
