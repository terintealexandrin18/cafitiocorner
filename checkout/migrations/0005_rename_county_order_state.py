# Generated by Django 3.2.25 on 2024-06-18 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='county',
            new_name='state',
        ),
    ]
