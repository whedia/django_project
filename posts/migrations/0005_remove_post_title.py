# Generated by Django 2.2 on 2020-09-14 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]