# Generated by Django 5.0 on 2023-12-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0006_product_branch_id_product_stock_delete_productstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]