# Generated by Django 3.1.7 on 2021-04-14 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20210414_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bets',
            options={'verbose_name': 'Bets'},
        ),
        migrations.AlterModelOptions(
            name='lots',
            options={'verbose_name': 'Lots'},
        ),
    ]
