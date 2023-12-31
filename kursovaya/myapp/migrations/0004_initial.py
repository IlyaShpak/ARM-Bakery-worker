# Generated by Django 5.0 on 2023-12-06 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0003_remove_products_list_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('addres', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fio', models.CharField(max_length=255)),
                ('post', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products_list',
            fields=[
                ('id', models.IntegerField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.customer')),
                ('products_name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('compound', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.IntegerField()),
                ('equipment_name', models.CharField(max_length=255)),
                ('equipment_state', models.CharField(max_length=255)),
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Raw',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('raw_name', models.CharField(max_length=255)),
                ('provider', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=255)),
                ('products_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.products_list')),
            ],
        ),
    ]
