# Generated by Django 3.1 on 2020-08-08 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KEF_App', '0002_teacher_query'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_query',
            name='query_author',
        ),
    ]