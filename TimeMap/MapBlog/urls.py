from django.urls import path
from . import views

urlpatterns = [
    path('', views.UseDemand_list, name='UseDemand_list'),
]