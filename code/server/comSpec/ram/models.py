from django.db import models

# Create your models here.


class Memory_info(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    fr = models.DecimalField("Frequency | GHz",max_digit=5,decimal_places=1)
    moduel_name = models.CharField("Moduel Name",max_length=50)
    data_rate = models.PositiveIntegerField()
    capacity = models.SmallPositiveIntegerField()
    amount = models.PositiveIntegerField(blank=True,null=True)
    prize = models.DecimalField(max_digits=6,decimal_places=2)
    slug = models.SlugField(unique=True,blank=True)


class Mem_form_factor(models.Model):
    name = models.CharField(max_length=50)

class Mem_tech(models.Model):
    name = models.CharField(max_length=50)

class Mem_brand(models.Model):
    name = models.CharField(max_length=50)