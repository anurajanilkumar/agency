# Generated by Django 5.0 on 2024-01-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0019_complaint_created_at_complaint_read_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(default='OPEN', max_length=30),
        ),
    ]
