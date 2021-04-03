from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('patient/',patient,name="patient"),
    path('newPatient/',newPatient,name="newPatient"),
    path('viewPatient/<int:id>',viewPatient,name="viewPatient"),
    path('existingPatient/',existingPatient,name="existingPatient"),

    path('addDoctor/',addDoctor,name="addDoctor"),
]
