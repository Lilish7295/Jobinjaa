from django.contrib.admin import ModelAdmin, register
from .models import Transaction

@register(Transaction)
class TransactionAdmin(ModelAdmin):
    pass
