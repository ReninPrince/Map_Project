from django.db import models

# Create your models here.
class maps(models.Model):
        Username = models.CharField("Username",max_length=128,blank=False)
        Password = models.CharField("Password",max_length=128,blank=False)
        #email = models.EmailField("    Email",max_length=264,unique=True)
