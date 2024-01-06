from django.contrib import admin
from .models import *

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class MetroAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class DistrictAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class RoomsAdmin(admin.ModelAdmin):
    search_fields = ('roomnum',)

admin.register(City, CityAdmin)
admin.register(Metro, MetroAdmin)
admin.register(District, DistrictAdmin)
admin.register(Rooms, RoomsAdmin)