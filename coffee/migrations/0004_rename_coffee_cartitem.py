# Generated by Django 5.0 on 2024-01-30 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_rename_quality_coffee_quantity_alter_coffee_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='coffee',
            new_name='CartItem',
        ),
    ]
