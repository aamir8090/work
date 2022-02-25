# Generated by Django 4.0 on 2022-02-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workconnect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('JOB', models.TextField()),
                ('Location', models.TextField()),
                ('Type', models.TextField()),
                ('pics', models.ImageField(upload_to='images/')),
                ('Description', models.TextField()),
            ],
        ),
    ]
