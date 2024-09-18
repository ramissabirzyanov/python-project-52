from django.test import TestCase
from django.urls import reverse
from task_manager.status.models import Status
from task_manager.user.models import User
from task_manager.status.forms import StatusCreateForm, StatusUpdateForm


class StatusViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='Bruce', last_name='Lee', username='water', password='1234')
        self.client.force_login(self.user)

    def test_statuses_list_view(self):
        response = self.client.get('/statuses/')
        self.assertEqual(response.status_code, 200)


class StatusModelTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name='готово')

    def test_name_label(self):
        status = Status.objects.get(id=1)
        field_label = status._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Имя')


class Status_CRUD_test(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='Bruce', last_name='Lee', username='water', password='1234')
        self.client.force_login(self.user)
        self.status = Status.objects.create(name='на тестировании')


    def test_get_status_create(self):
        response = self.client.get(reverse('status_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'status/status_create.html')

    def test_post_status_create(self):
        form_data = {
            'name': 'готово',
            }
        response = self.client.post(reverse('status_create'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='готово').exists())
        self.assertRedirects(response, '/statuses/')

    def test_get_status_update(self):
        response = self.client.get(reverse('status_update', args=[self.status.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'status/status_update.html')

    def test_post_status_update(self):
        new_form_data = {
            'name': 'приостановлена',
            }
        response = self.client.post(reverse('status_update', args=[self.status.id]), new_form_data)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'приостановлена')
        self.assertFalse(Status.objects.filter(name='на тестировании').exists())
        self.assertRedirects(response, '/statuses/')
        self.assertEqual(response.status_code, 302)

    def test_get_status_delete(self):
        response = self.client.get(reverse('status_delete', args=[self.status.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'status/status_delete.html')

    def test_post_status_delete(self):
        response = self.client.delete(reverse('status_delete', args=[self.status.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/statuses/')
        self.assertFalse(Status.objects.filter(name='приостановлена').exists())
