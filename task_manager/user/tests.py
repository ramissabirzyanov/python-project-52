from django.test import TestCase, Client
from django.urls import reverse
from task_manager.user.models import User


class UsersViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_users_list_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='Bruce',
            last_name='Lee',
            username='water',
            password='1234'
            )
        self.user.save()

    def test_username_label(self):
        u = User.objects.get(username='water')
        field_label = u._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'имя пользователя')


class User_CRUD_test(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='michael',
                                        last_name='caine',
                                        username='alfred',
                                        password='123',
                                        )
        self.client.force_login(self.user)

    def test_get_create_view(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_create.html')

    def test_post_create_view(self):
        form_data = {
            'first_name': 'jeckie',
            'last_name': 'chan',
            'username': 'legend',
            'password1': '123',
            'password2': '123',
            }
        response = self.client.post(reverse('user_create'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='legend').exists())
        self.assertRedirects(response, '/login/')

    def test_get_update_user(self):
        response = self.client.get(reverse('user_update', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_update.html')

    def test_post_update_user(self):
        new_form_data = {
            'first_name': 'michael',
            'last_name': 'caine',
            'username': 'gotem',
            'password1': '1234',
            'password2': '1234'
            }
        response = self.client.post(
            reverse('user_update', args=[self.user.id]),
            new_form_data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'gotem')
        self.assertFalse(User.objects.filter(username='alfred').exists())
        self.assertRedirects(response, '/users/')
        self.assertEqual(response.status_code, 302)

    def test_get_delete_user(self):
        response = self.client.get(reverse('user_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_delete.html')

    def test_post_delete_user(self):
        response = self.client.delete(
            reverse('user_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertFalse(User.objects.filter(username='gotem').exists())
