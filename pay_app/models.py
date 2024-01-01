from django.db import models


class Transaction(models.Model):
    transaction_date = models.DateField()
    amount = models.IntegerField()
    tracking_code = models.CharField(max_length = 8)
    payer = models.CharField(max_length = 100)
    payer_phone_number = models.CharField (max_length = 12)
    origin_card = models.CharField(max_length = 12)
    bank = models.CharField(max_length = 30)

    def __str__(self):
        return self.tracking_code
    


