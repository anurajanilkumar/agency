# Generated by Django 5.0 on 2023-12-30 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0001_user_branch_user_group_id_alter_user_contact_manager_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
