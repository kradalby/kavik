from django.contrib import admin
from apps.consultants.models import Consultant

# Register your models here.

class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('number', 'firstName', 'lastName', 'email', 'phone1')

admin.site.register(Consultant, ConsultantAdmin)
