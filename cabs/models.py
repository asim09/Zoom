from django.db import models
from operators.models import Operator

# Create your models here.

# MODEL_CHOICE = (
#     (1,'sedan'),
#     (2,'suv'),
#     (3,'tempo')
# )

class Cab(models.Model):
    # cab_type_id = models.IntegerField(choices=MODEL_CHOICE, default=1)
    cab_type_id = models.IntegerField()
    model_name = models.CharField(max_length=120,blank=False,null=False)
    model_number = models.CharField(max_length=120,blank=True, null=True)
    city = models.CharField(max_length=120,blank=False,null=False)
    seats = models.IntegerField()
    # operator_id = models.ManyToManyField(Operator,blank=False)
    operator_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    soft_delete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.model_name
