from django.contrib import admin

from taquilla_banco_api import models

admin.site.register(models.transferRequest)
admin.site.register(models.transferStatus)
