from django.contrib import admin
from .models import CalculationsBMI
from .models import CalculationsBDI
# Register your models here.
admin.site.register(CalculationsBMI)
admin.site.register(CalculationsBDI)