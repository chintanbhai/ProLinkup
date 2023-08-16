from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(register)
# admin.site.register(job)
@admin.register(job)
class jobAdmin(admin.ModelAdmin):
    list_display = ('company_name','email','address','time','salary')
    search_fields = ('company_name','salary')
    
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')
    search_fields = ('name',)
    
admin.site.register(Adminregister)
admin.site.register(candidate)
# admin.site.register(profile)

@admin.register(profile)
class profile(admin.ModelAdmin):
    list_display = ('user','apply_job','apply_date','apply_time')


@admin.register(applyjobs)
class applyjobs(admin.ModelAdmin):
    list_display = ('emp_id','jobs')
    search_fields = ('emp_id',)