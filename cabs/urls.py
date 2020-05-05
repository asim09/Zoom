from django.urls import path
from cabs.views import *

urlpatterns = [
    path('', show,name='cab_list'),
    path('add/', add,name='cab_add'),
    path('<int:id>/edit/', update,name='cab_edit'),
    path('<int:id>/delete/', delete,name='cab_delete'),
]
