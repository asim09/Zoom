from django.db import models

# Create your models here.

class Operator(models.Model):
    name = models.CharField(max_length=120,blank=False,null=False)
    city = models.CharField(max_length=120,blank=False,null=False)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=250)
    is_active = models.BooleanField(default=True)
    soft_delete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

