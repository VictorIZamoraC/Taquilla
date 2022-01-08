from django.contrib import admin
from taquilla_central_api.models import passesBoxOffice, passesSold

# Register your models here.

admin.site.register(passesBoxOffice)
admin.site.register(passesSold)