# Generated by Django 5.0 on 2023-12-30 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0002_delete_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Branch',
            new_name='branch_id',
        ),
    ]