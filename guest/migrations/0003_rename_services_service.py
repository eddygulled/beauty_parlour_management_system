# Generated by Django 4.0.3 on 2022-04-05 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_remove_appointment_services_appointment_service_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
