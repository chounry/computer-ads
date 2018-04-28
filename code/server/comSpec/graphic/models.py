from django.db import models
from motherboard.models import Expansion_connector

# Create your models here.
class API_supp(models.Model):
    name = models.CharField(max_length="50")
    version = models.CharField(max_length=3)

class GPU_brand(models.Model):
    name = models.CharField(max_length=100)

class Vram_type(models.Model):
    name = models.CharField(max_length=50)

class GPU(models.Model):
    name = models.CharField(max_length=50)

class Processor(models.Model):
    name = models.CharField(max_length=50,help_text="Stream Processor or CUDA or else")

class Graphic_info(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    num_of_cores = models.PositiveIntegerField("# of Cores",blank=True,null=True)
    core_clock = models.PositiveIntegerField(help_text="MHz unit")
    num_of_core = models.PositiveIntegerField("# Number of Cores",null=True,blank=True)
    memory_speed = models.CharField(help_text="eg: 7Gbs",max_length=3)
    memory_cap = models.CharField("Memory Capacity",max_length=4)
    memory_width = models.CharField("Memory Bandwidth",max_length=5)
    power = models.CharField(max_length=5)
    num_of_pin = models.CharField("# of Pin",max_length=5,help_text="eg:16 or 4")
    recom_power = models.CharField("Recommended Power",null=True, max_length=5,blank=True)
    slug = models.SlugField(unique=True)
    gpu_brand = models.ForeignKey(GPU_brand,on_delete=models.SET_NULL,blank=True,null=True)
    vram_type = models.ForeignKey(Vram_type,on_delete=models.SET_NULL,blank=True,null=True)
    gpu = models.ForeignKey(GPU,on_delete=models.SET_NULL,blank=True,null=True)
    api_supp = models.ManyToManyField(API_supp)
    processor = models.ForeignKey(Processor,on_delete=models.SET_NULL,blank=True,null=True)
    expansion_conn = models.ForeignKey(Expansion_connector, on_delete=models.SET_NULL,blank=True,null=True)





