# Generated by Django 5.0.3 on 2024-03-22 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_remove_offer_end_date_remove_offer_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='title',
        ),
        migrations.AddField(
            model_name='offer',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='offer',
            name='image_url',
            field=models.CharField(default='/offer.jpg', max_length=100),
        ),
        migrations.AddField(
            model_name='offer',
            name='original_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='offer',
            name='specialization',
            field=models.CharField(default='General', max_length=50),
        ),
    ]
