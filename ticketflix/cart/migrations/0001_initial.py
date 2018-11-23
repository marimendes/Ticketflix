# Generated by Django 2.0.8 on 2018-11-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticket', '0002_auto_20181119_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcial_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tickets', models.ManyToManyField(help_text='Tickets do Carrinho', to='ticket.Ticket', verbose_name='Ticket')),
            ],
            options={
                'verbose_name': 'Carrinho',
                'verbose_name_plural': 'Carrinhos',
            },
        ),
    ]