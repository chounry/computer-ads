from django.db import models

# Create your models here
class Market_info(models.Model):
    market_name = models.CharField(max_length=50)
    img = models.ImageField(max_length=200)

# class Image(models.Model):
#     f = models.ImageField(max_length=200)

#     mainboard = models.ForeignKey(Mainboard_info,on_delete=models.CASCADE,null=True,blank=True)
#     cpu = models.ForeignKey(CPU_info,on_delete=models.CASCADE,null=True,blank=True)
#     memory = models.ForeignKey(Memory_info,on_delete=models.CASCADE,null=True,blank=True)
#     graphic = models.ForeignKey(Graphic_info,on_delete=models.CASCADE,null=True,blank=True)
    
# class Market_link(models.Model):
#     market_link = models.URLField()

#     mainboard = models.ForeignKey(Mainboard_info,on_delete=models.CASCADE,null=True,blank=True)
#     cpu = models.ForeignKey(CPU_info,on_delete=models.CASCADE,null=True,blank=True)
#     memory = models.ForeignKey(Memory_info,on_delete=models.CASCADE,null=True,blank=True)
#     graphic = models.ForeignKey(Graphic_info,on_delete=models.CASCADE,null=True,blank=True)
#     market_info = models.ForeignKey(Market_info,on_delete=models.CASCADE)

# class Market_mem(models.Model):
#     amount = models.CharField(max_length=3)

#     market_link = models.OneToOneField(Market_link,on_delete=models.CASCADE,verbose_name='Market Link')