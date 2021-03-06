# Generated by Django 4.0.3 on 2022-04-05 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AptNumber', models.CharField(max_length=80)),
                ('Name', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=120)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('AptDate', models.DateTimeField(auto_now=True)),
                ('Services', models.CharField(max_length=120)),
                ('ApplyDate', models.DateTimeField(auto_now=True)),
                ('AptStrTime', models.CharField(default='', max_length=30)),
                ('Remark', models.CharField(max_length=250)),
                ('Status', models.CharField(max_length=50)),
                ('RemarkDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=200)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Location', models.CharField(max_length=200)),
                ('MapLocation', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=120)),
                ('Email', models.EmailField(max_length=120)),
                ('PhoneNumber', models.BigIntegerField()),
                ('Gender', models.CharField(max_length=1)),
                ('CreationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_one', models.CharField(max_length=500)),
                ('front_two', models.CharField(max_length=500)),
                ('front_title_one', models.CharField(max_length=500)),
                ('front_title_two', models.CharField(max_length=500)),
                ('footer_one', models.CharField(max_length=500)),
                ('about_details', models.CharField(default='', max_length=500)),
                ('service_details', models.CharField(default='', max_length=500)),
                ('contact_details', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=200)),
                ('Cost', models.FloatField()),
                ('CreationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillingId', models.CharField(max_length=10)),
                ('PostingDate', models.DateTimeField(auto_now=True)),
                ('ServiceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.services')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.customer')),
            ],
        ),
    ]
