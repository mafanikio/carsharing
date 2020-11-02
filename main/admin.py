from django.contrib import admin
from .models import Employee, Car, Order, Services, Detail

# Register your models here.
admin.site.register(Employee)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Services)
admin.site.register(Detail)
