from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class adSherlock_model(models.Model):

    names= models.CharField(max_length=300)
    App_Desc= models.CharField(max_length=300)
    Mobile_OS= models.CharField(max_length=300)
    App_Developer= models.CharField(max_length=300)
    App_Developed_Country= models.CharField(max_length=300)
    App_Uses= models.CharField(max_length=300)
    Allowed_Clicks= models.CharField(max_length=300)
    User_Name= models.CharField(max_length=300)
    System_IP_Address= models.CharField(max_length=300)
    Clicked_DT= models.CharField(max_length=300)
    No_Of_Time_Clicked= models.CharField(max_length=300)
    Like1= models.CharField(max_length=300)
    Rate= models.CharField(max_length=300)

class clickfraud_model(models.Model):

     names = models.CharField(max_length=300)
     App_Desc= models.CharField(max_length=300)
     Mobile_OS= models.CharField(max_length=300)
     App_Developer= models.CharField(max_length=300)
     App_Developed_Country= models.CharField(max_length=300)
     App_Uses= models.CharField(max_length=300)
     Allowed_Clicks= models.CharField(max_length=300)
     User_Name= models.CharField(max_length=300)
     System_IP_Address= models.CharField(max_length=300)
     Clicked_DT= models.CharField(max_length=300)
     No_Of_Time_Clicked= models.CharField(max_length=300)

class search_ratio_model(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



