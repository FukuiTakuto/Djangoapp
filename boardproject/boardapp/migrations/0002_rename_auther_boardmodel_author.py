# Generated by Django 3.2 on 2024-02-27 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='auther',
            new_name='author',
        ),
    ]
