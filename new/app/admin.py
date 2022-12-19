from django.contrib import admin
from .models import Dishes, Order, Hall


admin.site.register(Dishes)
admin.site.register(Order)
admin.site.register(Hall)