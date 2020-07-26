from django import forms
from django.forms import ModelForm, Select

from .models import Cab
from operators.models import Operator

def get_opearators(request):
    opr = Operator.objects.filter(soft_delete=0)
    print(opr)
    return opr

# class CabForm(forms.Form):
#     cab_type_id = forms.IntegerField()
#     model_name = forms.CharField()
#     model_number = forms.IntegerField()
#     city = forms.CharField()
#     seats = forms.IntegerField()
#     operator_id = forms.Select()
#     is_active = forms.BooleanField()

class CabForm(forms.ModelForm):
    class Meta:
        model = Cab

        fields = ['cab_type_id','model_name','model_number','city','seats','operator_id','is_active']

        widgets = {
            'operator_id': Select(),
        }

