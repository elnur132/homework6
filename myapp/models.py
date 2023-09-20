from django.db import models

class IceCreamShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class IceCream(models.Model):
    flavor = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.flavor
    


class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.BooleanField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


