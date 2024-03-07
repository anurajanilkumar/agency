from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('agencyapp', 'Group')
    Group.objects.create(group_name='CONSUMER')
    Group.objects.create(group_name='MANAGER')
    Group.objects.create(group_name='STAFF')

def create_branch(apps, schema_editor):
    Branch = apps.get_model('agencyapp','Branch')
    Branch.objects.create(branch_name='Kesi HQ', branch_location='Kochi')

class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
        migrations.RunPython(create_branch),
    ]
