from django.test import TestCase
from django.shortcuts import get_object_or_404, HttpResponse
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    
    def test_home_page_is_status_200(self):
        """
        Ensure url is not returning a status other than 200 and correct template is rendered
        """
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed("todo_list.html")
        
    def test_add_item_page_is_status_200(self):
        """
        Ensure url is not returning a status other than 200 and correct template is rendered
        """
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed("add_item.html")
        
    def test_edit_item_page_is_status_200(self):
        """
        Ensure url is not returning a status other than 200 and correct template is rendered
        """
        item = Item(name = "A test item")
        item.save()
        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed("add_item.html")
        
    def test_edit_item_page_is_status_404_if_item_does_not_exist(self):
        """
        Ensure url is returning a status of 404 if the item does not exist by using an id not in the database
        """
        page = self.client.get("/edit/{0}".format(1000))
        self.assertEqual(page.status_code, 404)
        self.assertTemplateUsed("add_item.html")
        
    def test_hello_page_returns_hello_world(self):
        """
        Ensure that "Hello World!" is returned
        """
        page = self.client.get("/hello")
        self.assertEqual(page.content, b"Hello World!")
    
    def test_post_add_an_item(self):
        """
        Ensure that item 'done' value is set to False
        """
        response = self.client.post("/add", {"name": "A test item"} )
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
    
    def test_post_edit_an_item_name(self):
        """
        Ensure that when editing an item name the new name is returned for that item
        """
        item = Item(name="A test item")
        item.save()
        id = item.id
        """
        Update the 'name' attribute for the current item using its id 
        """
        response = self.client.post("/edit/{0}".format(id), {"name": "A new name"} )
        item = get_object_or_404(Item, pk = id)
        self.assertEqual("A new name", item.name)
    
    def test_toggle_status(self):
        """
        Ensure that the status of the 'done' field is changed to True when the id of an item is passed to the toggle route with a False status
        """
        item = Item(name="A test item")
        item.save()
        id = item.id
        response = self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk = id)
        self.assertEqual(item.done, True)
    