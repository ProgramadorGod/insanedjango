from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, verbose_name='The Address')
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.name


class Articles(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return 'The name is %s, the section is %s and the price is %s' %(self.name, self.section, self.price)

class Tasks(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()
