# Generated by Django 4.2.1 on 2023-05-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='profile_icons/user_default.jpg', upload_to='profile_icons'),
        ),
    ]
