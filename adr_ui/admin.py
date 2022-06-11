from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Status, System, ADR, Influence, InfluenceADR

admin.site.register(Status)
admin.site.register(System)
admin.site.register(ADR)
admin.site.register(Influence)
admin.site.register(InfluenceADR)