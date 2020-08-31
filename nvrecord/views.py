from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Vehicle

from .models import NavigationRecord


def vehicle_list(request):
   template = loader.get_template('nvrecord/records.html')
   items = NavigationRecord.objects.all().select_related('vehicle').values('vehicle__plate', 'latitude' , 'longitude' , 'datetime')
   context = {
     'items' : items
   }
   return HttpResponse(template.render(context,request))
