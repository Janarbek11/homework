# Generated by Django 3.1.7 on 2021-04-14 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmcode',
            options={'verbose_name': 'Confirm Code'},
        ),
        migrations.AlterModelOptions(
            name='regsubsforlot',
            options={'verbose_name': 'Registered subscribers'},
        ),
    ]