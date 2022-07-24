# Generated by Django 4.0.4 on 2022-07-16 14:14

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultuser',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[accounts.validators.validate_phone]),
        ),
    ]