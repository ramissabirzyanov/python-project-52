# Generated by Django 5.1 on 2024-10-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0002_alter_label_options_alter_label_name'),
        ('task', '0010_remove_task_labels_task_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', to='label.label', verbose_name='Labels'),
        ),
    ]
