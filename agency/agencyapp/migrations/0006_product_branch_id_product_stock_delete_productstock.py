# Generated by Django 5.0 on 2023-12-30 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0005_product_productstock_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='branch_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='agencyapp.branch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductStock',
        ),
    ]