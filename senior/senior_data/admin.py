from django.contrib import admin
from . models import Senior #SearchSenior

# Register your models here


#admin.site.register(SearchSenior)
 
@admin.register(Senior)
class SeniorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('full_name',),}

