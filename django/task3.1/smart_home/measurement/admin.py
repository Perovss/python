from django.contrib import admin
from measurement.models import Sensor,Measurement

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', ]
    list_filter = ['id', 'name', 'description', ]
    search_fields = ['name', 'description', ]

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'created_at', 'sensor', ]
    list_filter = ['id', 'temperature', 'created_at',  'sensor', ]
    search_fields = ['temperature', 'created_at', 'sensor', ]