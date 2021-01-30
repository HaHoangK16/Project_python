# Generated by Django 3.1.5 on 2021-01-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(max_length=40)),
                ('phone', models.IntegerField(max_length=20)),
                ('storeaddress', models.CharField(max_length=100)),
            ],
        ),
    ]