from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductsTest(TestCase):
    """
    Test cases for the models in our products app
    """
    def test_str(self):
        """
        That our test_name is equal to the string we've defined
        """
        test_name = Product(name = "A Sample Product")
        self.assertEqual(str(test_name), "A Sample Product")
        
        