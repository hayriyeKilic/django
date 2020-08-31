from django.contrib import admin
from .models import Vehicle
from .models import NavigationRecord

admin.site.register(Vehicle)
admin.site.register(NavigationRecord)
