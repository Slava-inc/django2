from django.db import models


'''
CREATE TABLE PRODUCT(
    product_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL,
    price FLOAT NOT NULL
    
    PRIMARY KEY (product_id)
)
'''
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)

'''
CREATE TABLE STAFF(
    staff_id INT AUTO_INCREMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL
    
    PRIMARY KEY (staff_id)
)
'''
director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщица')
]
class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)
    labor_contract = models.IntegerField()

'''
CREATE TABLE ORDER(
    order_id INT AUTO_INCREMENT NOT NULL,
    time_in DATATIME NOT NULL,
    time_out DATATIME,
    cost FLOAT NOT NULL,
    take_away INT NOT NULL,
    staff INT NOT NULL,
    
    PRIMARY KEY(order_id),
    FOREIGN KEY(staff) REFERENCES STAFF(staff_id)
)
'''
class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='ProductOrder')


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, default=0)
    email = models.CharField(blank=True, max_length=50, default='')
    
    