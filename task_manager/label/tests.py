from django.test import TestCase
from django.urls import reverse
from task_manager.label.models import Label
from task_manager.user.models import User


class LabelViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='Robert', last_name='De Niro', username='driver', password='1234')
        self.client.force_login(self.user)

    def test_labels_list_view(self):
        response = self.client.get('/labels/')
        self.assertEqual(response.status_code, 200)


class LabelModelTest(TestCase):
    def setUp(self):
        self.status = Label.objects.create(name='test')

    def test_name_label(self):
        label = Label.objects.get(id=1)
        field_label_name = label._meta.get_field('name').verbose_name
        self.assertEqual(field_label_name, 'Имя')


class Label_CRUD_test(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='Robert', last_name='De Niro', username='driver', password='1234')
        self.client.force_login(self.user)
        self.label = Label.objects.create(name='label1')

    def test_get_label_create(self):
        response = self.client.get(reverse('label_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'label/label_create.html')

    def test_post_label_create(self):
        form_data = {
            'name': 'label2',
            }
        response = self.client.post(reverse('label_create'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name='label2').exists())
        self.assertRedirects(response, '/labels/')

    def test_get_label_update(self):
        response = self.client.get(reverse('label_update', args=[self.label.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'label/label_update.html')

    def test_post_label_update(self):
        new_form_data = {
            'name': 'label1 updated',
            }
        response = self.client.post(reverse('label_update', args=[self.label.id]), new_form_data)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'label1 updated')
        self.assertFalse(Label.objects.filter(name='label1').exists())
        self.assertRedirects(response, '/labels/')
        self.assertEqual(response.status_code, 302)

    def test_get_label_delete(self):
        response = self.client.get(reverse('label_delete', args=[self.label.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'label/label_delete.html')

    def test_post_label_delete(self):
        response = self.client.delete(reverse('label_delete', args=[self.label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/labels/')
        self.assertFalse(Label.objects.filter(name='label1 updated').exists())
