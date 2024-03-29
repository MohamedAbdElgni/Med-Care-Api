# Generated by Django 5.0.3 on 2024-03-22 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_remove_offer_description_remove_offer_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image_url',
            field=models.ImageField(default='offer_images/default.jpg', upload_to='offer_images/'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='original_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
