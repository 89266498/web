from django.contrib import admin

# Register your models here.
from .models import Contactor
from .models import Org,Elog

admin.site.register(Contactor)
admin.site.register(Org)
admin.site.register(Elog)