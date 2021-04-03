from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
   
    list_display = ['id','Test_name','qty','Patient']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
   
    list_display = ['id','name','date']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','name','date']