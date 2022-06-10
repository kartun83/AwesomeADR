from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Status, System, ADR

admin.site.register(Status)
admin.site.register(System)
admin.site.register(ADR)