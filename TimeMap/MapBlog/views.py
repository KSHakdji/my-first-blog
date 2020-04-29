from django.shortcuts import render
from django.utils import timezone
from .models import UseDemand

# Create your views here.

def UseDemand_list(request):
    usedemands = UseDemand.objects.filter(demand_time__lte=timezone.now()).order_by('demand_time')
    return render(request, 'MapBlog/UseDemand_list.html', {'usedemands':usedemands})