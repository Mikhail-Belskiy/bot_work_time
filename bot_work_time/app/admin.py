from django.contrib import admin

from django.contrib import admin
from .models import Location, Mark, User

admin.site.register(Location)
admin.site.register(Mark)
admin.site.register(User)
