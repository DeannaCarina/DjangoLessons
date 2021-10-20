from django.test import TestCase
from .forms import ItemForm


# class TestDjango(TestCase):

#     def test_this_thing_works1(self):
#         self.assertEqual(1, 0)


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors["name"][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test to do item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
