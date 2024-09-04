from django.test import TestCase, Client
from django.urls import reverse
from task_manager.user.models import User
from task_manager.user.forms import UserCreateForm 


class UsersViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_users_list_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='Bruce', last_name='Lee', username='water', password='1234')
        self.user.save()
    
    def test_username_label(self):
        u = User.objects.get(id=1)
        field_label = u._meta.get_field('username').verbose_name
        self.assertEqual(field_label,'имя пользователя')


class User_CRUD_test(TestCase):
    # fixtures = ["test_user.json"]
    def setUp(self):
        self.user = User.objects.create(first_name='michael', last_name='caine', username='alfred', password='123')
        self.user.save()

    def test_get_create_view(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_create.html')

    def test_post_create_view(self):
        form_data = UserCreateForm(data={
            'first_name': 'jeckie',
            'last_name': 'chan',
            'username': 'legend',
            'password1': '123',
            'password2': '123',
            }).data
        response = self.client.post(reverse('user_create'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='legend').exists())
        self.assertRedirects(response, '/login/')
    
    def test_get_update_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('user_update', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_update.html')

    def test_post_update_user(self):
        self.client.force_login(self.user)
        new_data = UserCreateForm(data={
            'first_name': 'michael',
            'last_name': 'caine',
            'username': 'gotem',
            'password1': '1234',
            'password2': '1234'
            }).data
        response = self.client.post(reverse('user_update', args=[self.user.id]), new_data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'gotem')
        self.assertFalse(User.objects.filter(username='alfred').exists())
        self.assertRedirects(response, '/users/')
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(id=self.user.id)
        
