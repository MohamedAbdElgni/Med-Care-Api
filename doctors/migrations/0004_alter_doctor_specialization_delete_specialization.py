# Generated by Django 5.0.3 on 2024-03-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_specialization_alter_doctor_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Specialization',
        ),
    ]