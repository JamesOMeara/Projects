from django.contrib import admin

# Register your models here.

from CarSharing_app.models import route, clientMessages, driver

admin.site.register(route)
