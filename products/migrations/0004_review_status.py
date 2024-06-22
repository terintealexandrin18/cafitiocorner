# Generated by Django 3.2.25 on 2024-06-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending', max_length=10),
        ),
    ]
