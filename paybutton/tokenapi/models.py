from django.db import models
# Create your models here.


class MerchantStore(models.Model):
    usr = models.CharField(max_length=15, unique=True)

    token = models.Manager()

    class Meta:
        verbose_name = 'user_field'
        db_table = 'merchant_store'

    def __str__(self):
        return self.usr


class MerchantInfo(models.Model):
    merchant_id = models.ForeignKey(MerchantStore, on_delete=models.CASCADE)
    merchant_callback_url = models.CharField(max_length=20, verbose_name='url_field', unique=True)

    def __str__(self):
        return self.merchant_callback_url
