# В файле myapp/admin.py
from django.contrib import admin
from .models import Customer, Worker, Raw, Products_list, Equipment


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['id', 'company_name', 'phone_number', 'addres']
    list_display = ['id', 'company_name', 'phone_number', 'addres']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['id', 'fio', 'post', 'phone_number', 'salary']
    list_display = ['id', 'fio', 'post', 'phone_number', 'salary']


@admin.register(Raw)
class RawAdmin(admin.ModelAdmin):
    search_fields = ['id', 'products_list', 'raw_name', 'provider', 'amount', 'unit']
    list_display = ['id', 'products_list', 'raw_name', 'provider', 'amount', 'unit']


@admin.register(Products_list)
class ProductListAdmin(admin.ModelAdmin):
    search_fields = ['id', 'customer', 'products_name', 'price', 'description', 'compound']
    list_display = ['id', 'customer', 'products_name', 'price', 'description', 'compound']


@admin.register(Equipment)
class EqupmentAdmin(admin.ModelAdmin):
    search_fields = ['id', 'equipment_name', 'equipment_state', 'worker']
    list_display = ['id', 'equipment_name', 'equipment_state', 'worker']