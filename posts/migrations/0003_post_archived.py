# Generated by Django 5.0.6 on 2024-05-23 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20240507_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
