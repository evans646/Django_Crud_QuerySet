# Generated by Django 4.1.2 on 2023-01-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_queryset', '0005_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-id']},
        ),
    ]
