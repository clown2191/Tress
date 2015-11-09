from django.contrib import admin

# Register your models here.
from altas.models import Corredor


class CorredorAdmin(admin.ModelAdmin):
	pass




admin.site.register(Corredor, CorredorAdmin)