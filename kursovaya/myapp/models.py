from django.db import models


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    addres = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class Products_list(models.Model):
    id = models.IntegerField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    products_name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    compound = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class Raw(models.Model):
    id = models.IntegerField(primary_key=True)
    products_list = models.ForeignKey(Products_list, on_delete=models.CASCADE)
    raw_name = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    amount = models.IntegerField()
    unit = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class Worker(models.Model):
    id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    salary = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Equipment(models.Model):
    id = models.IntegerField()
    equipment_name = models.CharField(max_length=255)
    equipment_state = models.CharField(max_length=255)
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.id)
