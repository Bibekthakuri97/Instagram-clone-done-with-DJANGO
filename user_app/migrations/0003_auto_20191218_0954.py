# Generated by Django 2.2 on 2019-12-18 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20191218_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
