# Generated by Django 5.0.3 on 2024-03-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, default='/profile.jpeg', null=True, upload_to='profile_images/'),
        ),
    ]