from django.db import models

class Store(models.Model):
    STORE_TYPE_CHOICES = (
        ('Grocery', 'Grocery'),
        ('Pharmacy', 'Pharmacy'),
        ('Clothing', 'Clothing'),
        ('Electronics', 'Electronics'),
        ('Furniture', 'Furniture'),
    )
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='stores/%Y/%m/%d', null=True, blank=True)
    type = models.CharField(max_length=20, choices=STORE_TYPE_CHOICES)

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    tags = models.ManyToManyField(ProductTag)

    def __str__(self):
        return self.name