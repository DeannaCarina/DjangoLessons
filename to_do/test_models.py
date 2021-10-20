from django.test import TestCase
from .models import Item


# class TestDjango(TestCase):

#     def test_this_thing_works1(self):
#         self.assertEqual(1, 0)


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name="Test to do item")
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name="Test to do item")
        self.assertEqual(str(item), 'Test to do item')

