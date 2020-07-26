from django.views.generic import ListView

from django.shortcuts import render,get_object_or_404
from operators.forms import OpeatorForm
from .models import Operator
from django.urls import reverse

from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

class Operator_list(ListView):
    queryset = Operator.objects.filter(soft_delete=0)
    template_name = 'operators/list.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        return context


def show(request):
    data = Operator.objects.filter(soft_delete=0)
    context = {}
    context['data'] = data
    return render(request,'operators/list.html',context)


def update(request,id=None):
    o = get_object_or_404(Operator,id=id)
    if request.method == 'POST':
        operator_form = OpeatorForm(request.POST or None, instance=o)
        if operator_form.is_valid():
            operator_form.save()
            return HttpResponseRedirect(reverse('operator_list'))

    data = OpeatorForm(instance=o)
    return render(request,'operators/edit.html',{'data':data})



def add(request):
    if request.method == 'POST':
        operator_form = OpeatorForm(request.POST)
        if operator_form.is_valid():
            operator_form.save()
            return HttpResponseRedirect(reverse('operator_list'))
    operator_form = OpeatorForm()
    return render(request,'operators/add.html',{'operator_form':operator_form})


def delete(request,id=None):
    o = get_object_or_404(Operator,id=id)
    o.soft_delete = 1
    o.save()
    return HttpResponseRedirect(reverse('operator_list'))


