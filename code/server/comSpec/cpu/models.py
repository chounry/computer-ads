from django.db import models

# Create your models here.

class CPU_info(models.Model):
    name = models.CharField(help_text="i5-3470",max_length=30)
    proc_num = models.CharField("Processor Number",help_text="3470",max_length="30")
    num_of_thread = models.PositiveSmallIntegerField("Number of Threads")
    base_fr = models.DecimalField("Base Frequency",max_digits=4,decimal_places=1)
    cache = models.PositiveSmallIntegerField("Cache")
    tdp = models.PositiveSmallIntegerField("Power Consumtion")
    max_memory = models.PositiveSmallIntegerField()
    num_of_mem_chann = models.PositiveSmallIntegerField("# of Memory Channels")
    max_mem_bandwidth = models.CharField("Max Memory bandwidth",max_length=5)
    prize = models.DecimalField(max_digits=6,decimal_places=2)
    slug = models.SlugField(unique=True,blank=True)
    
class CPU_model(models.Model):
    name = models.CharField(help_text="i5 or i3",max_length=30)

class CPU_gen(models.Model):
    name = models.CharField("CPU Generation",help_text="2 or else",max_length=10)

class Vertical_segment(models.Model):
    name = models.CharField("Vertical Segment",help_text="Desktop or Mobile",max_length=50)

class Series(models.Model):
    name = models.CharField("Series",help_text="HQ or K",max_length=20)

class Num_of_core(models.Model):
    amount = models.PositiveSmallIntegerField()
    name = models.CharField(blank=True, max_length=50)

class CPU_brand(models.Model):
    name = models.CharField("Brand Name",max_length=50)

class Socket_type(models.Model):
    name = models.CharField("Socket Type",max_length=50)
