from django.test import TestCase
from django.urls import reverse
from task_manager.status.models import Status
from task_manager.user.models import User
from task_manager.task.models import Task


class TaskViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='Robert', last_name='De Niro', username='taxi', password='123')
        self.client.force_login(self.user)

    def test_task_list_view(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='Robert', last_name='De Niro', username='taxi', password='123')
        self.client.force_login(self.user)
        self.status = Status.objects.create(name='тест')
        self.task = Task.objects.create(name='LOTR', status=self.status, author=self.user)
        
    def test_name_label(self):
        task = Task.objects.get(id=1)
        field_name = task._meta.get_field('name').verbose_name
        field_author = task._meta.get_field('author').verbose_name
        field_status = task._meta.get_field('status').verbose_name
        self.assertEqual(field_name, 'Имя')
        self.assertEqual(field_author, 'Автор')
        self.assertEqual(field_status, 'Статус')


class Task_CRUD_test(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='Al', last_name='Pacino', username='Scarface', password='123')
        self.client.force_login(self.user)
        self.status1 = Status.objects.create(name='test_status1')
        self.status2 = Status.objects.create(name='test_status2')
        self.task = Task.objects.create(name='The matrix', status_id=self.status1.id, author_id=self.user.id)


    def test_get_task_create(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_create.html')

    def test_post_task_create(self):
        task_count = Task.objects.count()
        form_data = {
            'name': 'Totoro',
            'description': 'must watch it!',
            'status': self.status2.id
            }
        response = self.client.post(reverse('task_create'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), task_count+1)
        self.assertTrue(Task.objects.filter(name='Totoro').exists())
        task = Task.objects.get(name='Totoro')
        self.assertEqual(task.author_id, self.user.id)
        self.assertRedirects(response, '/tasks/')
        self.assertEqual(task.status.name, 'test_status2')
        task_detail_resp = self.client.get(reverse('task_detail', args=[task.id]))
        self.assertEqual(task_detail_resp.status_code, 200)


    def test_get_task_update(self):
        response = self.client.get(reverse('task_update', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_update.html')

    def test_post_task_update(self):
        new_form_data = {
            'name': 'The matrix has you',
            'description': 'follow the white rabbit',
            'status': self.status2.id,
            }
        response = self.client.post(reverse('task_update', args=[self.task.id]), new_form_data)
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.description, 'follow the white rabbit')
        self.assertEqual(self.task.status.name, 'test_status2')
        self.assertFalse(Task.objects.filter(name='The matrix').exists())
        self.assertRedirects(response, '/tasks/')

    def test_get_task_delete(self):
        response = self.client.get(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_delete.html')

    def test_post_task_delete(self):
        response = self.client.delete(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/tasks/')
        self.assertFalse(Status.objects.filter(name='The matrix has you').exists())
