# Generated by Django 5.0.3 on 2024-03-12 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
