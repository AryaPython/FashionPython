# Generated by Django 4.1.7 on 2023-03-08 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_rename_img_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='img',
            new_name='image',
        ),
    ]
