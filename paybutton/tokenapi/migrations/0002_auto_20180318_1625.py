# Generated by Django 2.0 on 2018-03-18 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tokenapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantinfo',
            name='merchant_callback_url',
            field=models.CharField(max_length=20, unique=True, verbose_name='url_field'),
        ),
        migrations.AlterField(
            model_name='merchantinfo',
            name='merchant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokenapi.MerchantStore', unique=True),
        ),
        migrations.AlterField(
            model_name='merchantstore',
            name='usr',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
