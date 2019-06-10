from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig

class TestToDoApp(TestCase):
    
    def test_todo_app_name(self):
        """
        Ensure that the name of the app matches the name configured in app.py
        """
        self.assertEqual("todo", TodoConfig.name)
        self.assertEqual("todo", apps.get_app_config("todo").name)