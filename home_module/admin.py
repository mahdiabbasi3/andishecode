from django.contrib import admin
from . import models

admin.site.register(models.site_setting)

admin.site.register(models.UseFulLink)
admin.site.register(models.SocialMedia)
admin.site.register(models.License)