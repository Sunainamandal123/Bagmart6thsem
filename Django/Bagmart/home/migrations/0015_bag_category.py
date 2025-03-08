# Generated by Django 5.1.5 on 2025-03-06 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_bag_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='category',
            field=models.CharField(choices=[('school', 'School/College Bag'), ('luggage', 'Luggage'), ('hand_bag', 'Hand Bag'), ('duffle', 'Duffle Bag'), ('others', 'Others')], default='school', max_length=20),
        ),
    ]
