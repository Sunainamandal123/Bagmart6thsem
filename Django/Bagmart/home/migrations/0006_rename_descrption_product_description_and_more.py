# Generated by Django 5.1.5 on 2025-03-03 16:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_product_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0.001)]),
        ),
    ]
