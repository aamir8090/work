# Generated by Django 4.0 on 2022-02-20 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workconnect', '0006_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Email',
            new_name='Password',
        ),
    ]
