from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Item
from .forms import NewItemForm, EditItemForm
from .views import new, edit

class ItemAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.category = Category.objects.create(name='Test Category')

    def test_new_item_form_valid(self):
        form_data = {
            'category': self.category.id,
            'name': 'Test Item',
            'description': 'Description for the test item',
            'price': 10.99,
        }
        form = NewItemForm(data=form_data, files={'image': None})
        self.assertTrue(form.is_valid())

    def test_new_item_form_invalid_with_missing_required_fields(self):
        form_data = {}
        form = NewItemForm(data=form_data, files={'image': None})
        self.assertFalse(form.is_valid())
        
    def test_new_item_form_invalid_with_invalid_fields(self):
        form_data = {
            'category': self.category.id,
            'name': 'Test Item',
            'description': 'Description for the test item',
            'price': 'abc',
        }
        form = NewItemForm(data=form_data, files={'image': None})
        self.assertFalse(form.is_valid())        
        

    def test_edit_item_form_valid(self):
        item = Item.objects.create(
            category=self.category,
            name='Test Item',
            description='Description for the test item',
            price=10.99,
            created_by=self.user,
        )

        form_data = {
            'category': self.category.id,
            'name': 'Updated Test Item',
            'description': 'Updated description',
            'price': 15.99,
        }

        form = EditItemForm(data=form_data, instance=item, files={'image': None})
        
        if not form.is_valid():
            print(form.errors)
        
        self.assertTrue(form.is_valid())


    def test_edit_item_form_invalid(self):
        item = Item.objects.create(
            category=self.category,
            name='Test Item',
            description='Description for the test item',
            price=10.99,
            created_by=self.user,
        )

        form_data = {}
        form = EditItemForm(data=form_data, instance=item, files={'image': None})
        self.assertFalse(form.is_valid())

    def test_new_item_view(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('item:new'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], NewItemForm)

    def test_edit_item_view(self):
        self.client.login(username='testuser', password='testpassword')

        item = Item.objects.create(
            category=self.category,
            name='Test Item',
            description='Description for the test item',
            price=10.99,
            created_by=self.user,
        )

        response = self.client.get(reverse('item:edit', args=[item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], EditItemForm)