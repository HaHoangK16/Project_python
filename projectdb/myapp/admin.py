from django.contrib import admin

# Register your models here.
from .models import Staff
from .models import Store

admin.site.register(Staff)
admin.site.register(Store)

