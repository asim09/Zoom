from django.shortcuts import render,get_object_or_404
from operators.forms import OpeatorForm
from .models import Cab
from django.urls import reverse
from .forms import CabForm,get_opearators

from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    print('hi----------')
    return render(request,'cabs/list.html')

# def show(request):
#     data = Cab.objects.filter(soft_delete=0)
#     context = {}
#     context['data'] = data
#     return render(request,'cabs/list.html',context)


# def update(request,id=None):
#     o = get_object_or_404(Cab,id=id)
#     if request.method == 'POST':
#         operator_form = CabForm(request.POST or None, instance=o)
#         if operator_form.is_valid():
#             operator_form.save()
#             return HttpResponseRedirect(reverse('cab_list'))

#     data = CabForm(instance=o)
#     return render(request,'cabs/edit.html',{'data':data})


# def add(request):
#     print('---1-----')
#     opr_list = get_opearators(request)
#     # print(opr_list)
#     context = {}
#     for i in opr_list:
#         print(i.name, i.city)
#     if request.method == 'POST':
#         operator_form = CabForm(request.POST)
#         print (operator_form)
#         if operator_form.is_valid():
#             operator_form.save()
#             return HttpResponseRedirect(reverse('cab_list'))
#     operator_form = CabForm()
#     context['opr'] = opr_list
#     context['operator_form'] = operator_form
#     return render(request,'cabs/add.html',context)


# def delete(request,id=None):
#     o = get_object_or_404(Cab,id=id)
#     o.soft_delete = 1
#     o.save()
#     return HttpResponseRedirect(reverse('cab_list'))
