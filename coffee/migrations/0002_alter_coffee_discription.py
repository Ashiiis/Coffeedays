# Generated by Django 5.0 on 2024-01-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='discription',
            field=models.CharField(max_length=200),
        ),
    ]