from django.db import models
from django.utils.timezone import now


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories(self):
        return Category.objects.all()

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=32)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Products(models.Model):

    class Meta:
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=60)
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)

    @staticmethod
    def get_products_by_id(product_id):
        return Products.objects.filter(id__in=product_id)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_product_by_category(category):
        if category:
            return Products.objects.filter(category=category)
        else:
            return Products.get_all_products()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=now)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer):
        return Order.objects.filter(customer=customer).order_by('-date')

    def __str__(self):
        return f'{self.customer} ({self.date})'
