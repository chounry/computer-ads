from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from market.models import Market_info

class Mem_form_factor(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Mem_tech(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Mem_brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Module_type(models.Model):
    module_name = models.CharField("Moduel Name",max_length=50)
    cycle_time = models.CharField(max_length=50,help_text='Unit: ns')
    transfer_time = models.CharField(max_length=50,help_text='**Unit: ns')
    command_rate = models.CharField(max_length=50,help_text='**Unit: MHz')

    def __str__(self):
        return self.module_name + ' ' + self.command_rate

class Memory_info(models.Model):
    module_type = models.ForeignKey(Module_type,on_delete=models.PROTECT,null=True)

    series = models.CharField(max_length=50, default='---', blank=True)
    model_num = models.CharField("Item Model Number",blank=True,max_length=100,default='---')
    capacity = models.PositiveSmallIntegerField(help_text="Unit: GB")
    slug = models.SlugField(unique=True,blank=True)
    num_of_pin = models.PositiveSmallIntegerField("Number of Pin")
    voltage = models.CharField(max_length=100,help_text="**Unit: V",blank=True,default='---')
    
    mem_brand = models.ForeignKey(Mem_brand,on_delete=models.CASCADE,verbose_name='Memory Brand')
    mem_tech = models.ForeignKey(Mem_tech,on_delete=models.CASCADE,verbose_name='Memory Technology')
    mem_form_factor = models.ForeignKey(Mem_form_factor,on_delete=models.CASCADE,verbose_name='Memory Form Factor')

    def get_absolute_url(self):
        return reverse('ram:ram_detail',kwargs={'slug': self.slug})

    def save(self,*args,**kwargs):
        # tmp for preventing null value
        if not self.slug:
            tmp_module_name = self.moduel_name if self.moduel_name else ' '
            tmp_model_num = self.model_num if self.model_num else ' '
            self.slug = slugify("%s %s %s %s %s %s"%(self.mem_brand.name, tmp_model_num, tmp_module_name, self.fr, self.capacity, self.series))
        super(Memory_info, self).save(*args,**kwargs)
    def __str__(self):
        return self.mem_brand.name+ ' '+ self.series + ' ' + self.mem_tech.name + ' ' + str(self.capacity)+'GB'

class Image(models.Model):
    image = models.ImageField()
    ram = models.ForeignKey(Memory_info,on_delete=models.CASCADE)

class Memory_market(models.Model):
    link = models.URLField(max_length=2000)
    prize = models.DecimalField(max_digits=7,decimal_places=2)  
    quntity = models.PositiveSmallIntegerField()  

    memory = models.OneToOneField(Memory_info,on_delete=models.CASCADE)
    market = models.ForeignKey(Market_info,on_delete=models.CASCADE)