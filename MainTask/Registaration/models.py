from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from datetime import date 


class countrymodel(models.Model):
    cname = models.CharField(max_length = 50,null=True)
    

class statemodel(models.Model):
    country_id= models.ForeignKey(countrymodel, on_delete=models.CASCADE)
    sname = models.CharField(max_length = 50,null=True)

    def __str__(self):
        return self.sname


class checkbox(models.Model):
    boxname = models.CharField(max_length = 50,null=True)
    isactive = models.BooleanField(default=True)

class checkboxmany(models.Model):
    boxname_id = models.ForeignKey(checkbox, on_delete=models.CASCADE,null=True,related_name='topic_boxname_id')
    hobbies_id = models.ManyToManyField(checkbox)

class Employeecrud(models.Model):   
    Firstname = models.CharField(max_length=255,null=True)
    Lastname = models.CharField(max_length=255,null=True)
    mobile_no = models.CharField(max_length=255,null=True)
    choices = (('male','male'),('female','female'))
    gender = models.CharField(max_length=50,choices=choices,default = 'male')
    email = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    countryId = models.ForeignKey(countrymodel, on_delete=models.CASCADE,null=True)
    stateId = models.ForeignKey(statemodel, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='MainTask/static/', blank=True, null=True,verbose_name='photo')
    dateofbirth = models.DateField(auto_now=False, auto_now_add=False, null=True)
    dateofjoining = models.DateField(auto_now=False, auto_now_add=False, null=True)
    isactive  = models.BooleanField(default=True)
    



# class hobbies(models.Model):
#     boxnameId = models.ForeignKey(role, on_delete=models.CASCADE,null=True)
#     hobbies_id = models.ManyToManyField(Employeecrud)