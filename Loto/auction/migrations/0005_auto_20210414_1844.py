# Generated by Django 3.1.7 on 2021-04-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20210414_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lots',
            options={'verbose_name': 'Lot'},
        ),
        migrations.AlterField(
            model_name='bets',
            name='lot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.lotsstatus'),
        ),
        migrations.AlterField(
            model_name='bets',
            name='subs_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.subscriber'),
        ),
    ]
