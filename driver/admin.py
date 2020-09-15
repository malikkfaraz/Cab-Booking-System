from django.contrib import admin

from driver.models import Driver, DriverLocation, DriverRidesHistory

admin.site.register(Driver)
admin.site.register(DriverLocation)
admin.site.register(DriverRidesHistory)
