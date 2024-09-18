from django.test import TestCase, Client
from django.urls import reverse
from task_manager.status.models import Status
from task_manager.user.models import User
from task_manager.task.models import Task
from task_manager.task.forms import TaskCreateForm, TaskUpdateForm


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
        self.status1 = Status.objects.create(name='готово')
        self.status2 = Status.objects.create(name='в процессе')
        self.task = Task.objects.create(name='The matrix', status=self.status1, author=self.user)


    def test_get_task_create(self):
        response = self.client.get(reverse('task:task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_create.html')

    def test_post_task_create(self):
        form_data = TaskCreateForm(data={
            'name': 'Totoro',
            'description': 'must watch it!',
            'status': self.status2,
            }).data
        response = self.client.post(reverse('task_create'), form_data, follow=True)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='Totoro').exists())
        task = Task.objects.get(name='Totoro')
        self.assertEqual(task.author_id, self.user.id)
        self.assertEqual(task.author.first_name, 'Al')
        self.assertRedirects(response, '/tasks/')
        self.assertEqual(task.status, 'в процессе')

    def test_get_task_update(self):
        response = self.client.get(reverse('task_update', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_update.html')

    def test_post_task_update(self):
        new_form_data = TaskUpdateForm(data={
            'name': 'The matrix has you',
            'description': 'follow the white rabbit',
            }).data
        response = self.client.post(reverse('task_update', args=[self.task.id]), new_form_data, follow=True)
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.description, 'follow the white rabbit')
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
