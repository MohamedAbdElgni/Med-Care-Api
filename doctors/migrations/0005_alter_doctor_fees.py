# Generated by Django 5.0.3 on 2024-03-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_alter_doctor_specialization_delete_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='fees',
            field=models.IntegerField(blank=True, default=200, null=True),
        ),
    ]
