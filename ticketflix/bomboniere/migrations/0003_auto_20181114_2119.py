# Generated by Django 2.0.8 on 2018-11-14 21:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bomboniere', '0002_combo_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='quantity',
            field=models.IntegerField(default=0, help_text='Quantidade de Itens em Estoque', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, help_text='Quantidade de Itens em Estoque', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade'),
        ),
    ]
