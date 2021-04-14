from django.contrib import admin
from .models import Subscriber, Bets, Lots, BetStatus, LotsStatus, ConfirmCode, RegSubsForLot, LotsHistory, Categories


admin.site.register(Subscriber)
admin.site.register(Bets)
admin.site.register(Lots)
admin.site.register(BetStatus)
admin.site.register(LotsStatus)
admin.site.register(ConfirmCode)
admin.site.register(RegSubsForLot)
admin.site.register(LotsHistory)
admin.site.register(Categories)
