# Generated by Django 2.2 on 2020-09-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(default=True, help_text='Nom du joueur', max_length=120),
            preserve_default=False,
        ),
    ]
