from django.db import models

# Create your models here.

class Mainboard(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    chipset = models.CharField(max_length=30)
    cpu_des = models.CharField("CPU Description",max_length=200)
    num_of_mem_slot = models.PositiveSmallIntegerField("# of Memory Slots")
    max_size = models.CharField(max_length=250)
    memmory_des = models.CharField("Memory Description",max_length=500)
    rear_panel_des = models.CharField("Rear Panel Description",max_length=350)
    expand_slot_des = models.CharField("Expansion Slot Description",max_length=500)
    audio_des = models.CharField("Audio Description",max_length=300)
    interal_des = models.CharField("Interal I\O Connector",max_length=1000)
    prize = models.DecimalField(max_digits=6,decimal_places=2)
    slug = models.SlugField(unique=True,blank=True)


#---- the 4 under is for mainboard only ----
class OnBoard_gpu(models.Model):
    description = models.CharField("On Board GPU",max_length=400)

class Multi_gpu(models.Model):
    description = models.CharField("Multi GPU",max_length=150)

class Storage(models.Model):
    description = models.CharField("Storage",max_length=500)

class Form_factor(models.Model):
    desctiption = models.CharField("Form Factor",max_length=50)

class Num_of_chan(models.Model):
    num_of_chan = models.PositiveSmallIntegerField()
    chan_name = models.CharField(max_length=30)


#---- this for other table also -----
class Expansion_connector(models.Model):
    name = models.CharField(help_text="eg: PCI or PCIe",max_length=30)
    version = models.DecimalField(max_digits=3,decimal_places=1)

class Expansion_pin(models.Model):
    pin_num = models.CharField(help_text="x1 | x16",max_length=5)

class Market_link(models.Model):
    market_name = models.CharField(max_length=50)
    link_url = models.CharField(max_length=400)




