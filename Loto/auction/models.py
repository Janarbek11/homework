from django.db import models
from datetime import datetime, timezone


class Subscriber(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)


class Bets(models.Model):
    subs_id = models.ForeignKey('Subscriber', on_delete=models.DO_NOTHING)
    lot_id = models.ForeignKey('LotsStatus', on_delete=models.DO_NOTHING)
    add_date = models.DateTimeField(auto_now_add=True)
    status_id = models.ForeignKey('BetStatus', on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Bet"


class Lots(models.Model):
    msisdn = models.CharField(max_length=13, blank=False)
    status_id = models.ForeignKey('LotsStatus', on_delete=models.DO_NOTHING)
    start_price = models.IntegerField()
    nomimal_price = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(year=2999, month=1, day=1, tzinfo=timezone.utc))
    category_id = models.ForeignKey('Categories', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "Lot"


class BetStatus(models.Model):
    name = models.CharField(max_length=200)


class LotsStatus(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class ConfirmCode(models.Model):
    subs_id = models.ForeignKey('Subscriber', on_delete=models.DO_NOTHING)
    code = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Confirm Code"


class RegSubsForLot (models.Model):
    subs_id = models.ForeignKey('Subscriber', on_delete=models.DO_NOTHING)
    lot_id = models.ForeignKey('Lots', on_delete=models.DO_NOTHING)
    add_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Registered subscribers"


class LotsHistory(models.Model):
    lot_id = models.ForeignKey('Lots', on_delete=models.DO_NOTHING)
    status_id = models.IntegerField()


class Categories(models.Model):
    name = models.CharField(max_length=50)
    bet_size = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
