from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from item.models import Category, Item
from conversation.models import Conversation, ConversationMessage
from conversation.forms import ConversationMessageForm
from django.core.files.uploadedfile import SimpleUploadedFile

class ConversationAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.category = Category.objects.create(name='Test Category')

        image_file = SimpleUploadedFile(
            "image.jpg",
            b"file_content",
            content_type="image/jpeg"
        )

        self.item = Item.objects.create(
            category=self.category,
            name='Test Item',
            description='Description for Test Item',
            price=10.99,
            created_by=self.user,
            image=image_file  
        )

    def test_new_conversation_view(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('conversation:new', args=[self.item.pk]))

        self.assertEqual(response.status_code, 302)

    def test_inbox_view(self):
        self.client.login(username='testuser', password='testpassword')

        conversation = Conversation.objects.create(item=self.item)
        conversation.members.add(self.user)
        conversation.members.add(self.item.created_by)
        conversation.save()

        response = self.client.get(reverse('conversation:inbox'))

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['conversations'],
            [conversation],
            transform=lambda x: x
        )

    def test_detail_view(self):
        self.client.login(username='testuser', password='testpassword')

        conversation = Conversation.objects.create(item=self.item)
        conversation.members.add(self.user)
        conversation.members.add(self.item.created_by)
        conversation.save()

        response = self.client.get(reverse('conversation:detail', args=[conversation.pk]))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['conversation'], conversation)
        self.assertIsInstance(response.context['form'], ConversationMessageForm)

    def test_new_conversation_form_valid(self):
        form_data = {'content': 'Test message'}
        form = ConversationMessageForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_new_conversation_form_invalid(self):
        form_data = {'content': ''}
        form = ConversationMessageForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_detail_form_valid(self):
        conversation = Conversation.objects.create(item=self.item)
        conversation.members.add(self.user)
        conversation.members.add(self.item.created_by)
        conversation.save()

        form_data = {'content': 'Test message'}
        form = ConversationMessageForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_detail_form_invalid(self):
        form_data = {'content': ''}
        form = ConversationMessageForm(data=form_data)

        self.assertFalse(form.is_valid())