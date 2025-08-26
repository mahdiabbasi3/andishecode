from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Plan)
admin.site.register(models.feature)

class PlanAdmin(admin.ModelAdmin):
    pass