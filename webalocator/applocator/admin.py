from django.contrib import admin
from applocator.models import PointOfInterest


class PointOfInterestAdmin(admin.ModelAdmin):
    model = PointOfInterest


admin.register(PointOfInterest, PointOfInterestAdmin)
