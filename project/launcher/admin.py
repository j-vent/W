from django.contrib import admin
from launcher.models import Housing

# Register your models here.
class HousingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Housing, HousingAdmin)