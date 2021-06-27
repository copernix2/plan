from django.contrib import admin
from .models import Cases

# Register your models here.

class CasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Cases, CasesAdmin)