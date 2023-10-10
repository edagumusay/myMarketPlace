from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from item.models import Category, Item
from dashboard.views import index
from django.core.files.uploadedfile import SimpleUploadedFile

class DashboardAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.category = Category.objects.create(name='Test Category')

        self.client.login(username='testuser', password='testpassword')

    def test_index_view_with_items(self):
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        item1 = Item.objects.create(
            name='Item 1',
            description='Description for Item 1',
            price=10.99,
            created_by=self.user,
            category=self.category,
            image=image_file 
        )

        item2 = Item.objects.create(
            name='Item 2',
            description='Description for Item 2',
            price=15.99,
            created_by=self.user,
            category=self.category,
            image=image_file 
        )

        response = self.client.get(reverse('dashboard:index'))

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['items'].order_by('name'),
            [item1, item2],
            transform=lambda x: x
        )

    def test_index_view_without_items(self):
        response = self.client.get(reverse('dashboard:index'))

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['items'],
            []
        )