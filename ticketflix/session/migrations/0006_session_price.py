# Generated by Django 2.0.8 on 2018-11-21 17:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0005_merge_20181120_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='price',
            field=models.FloatField(default=0, help_text='Preço', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
    ]
