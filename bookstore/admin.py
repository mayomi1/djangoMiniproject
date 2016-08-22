from django.contrib import admin
from . models import *


class AddbookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Addbook, AddbookAdmin)

