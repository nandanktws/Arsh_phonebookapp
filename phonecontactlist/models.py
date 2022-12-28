from django.db import models

    
class Phone_list(models.Model):
    name=models.CharField( max_length=50)
    contact_number = models.CharField(max_length=50)