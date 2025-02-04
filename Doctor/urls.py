from django.urls import path

from . import views

urlpatterns = [
    path('', views.doctor, name='doctor'),
    path('doctor/appostaff', views.appostaff, name='appostaff'),
    path('doctor/Labdash', views.Labdash, name='Labdash'),
    path('doctor/Equipdash', views.Equipdash, name='Equipdash'),
    path('doctor/Meddash', views.Meddash, name='Meddash'),
    path('doctor/patientdash', views.patientdash, name="patientdash"),

    path('doctor/addappo', views.addappo, name='addappo'),
    path('doctor/addlab', views.addlab, name='addlab'),
    path('doctor/addmed', views.addmed, name='addmed'),
    path('doctor/addequip', views.addequip, name='addequip'),
    path('doctor/addpat/', views.addpat, name="addpat"),


    path('api/add_appointment/', views.AddAppointmentView.as_view(), name='add_appointment'),  # API endpoint
    path('api/add_lab/', views.AddLabView.as_view(), name='add_lab'),
    path('api/add_equip/', views.AddEquipView.as_view(), name='add_equip'),
    path('api/add_med/', views.AddMedView.as_view(), name='add_med'),
    path('api/addpat/', views.AddPatientView.as_view(), name='add_pat'),

    path('doctor/report', views.report, name='report'),


    path('api/delete_appointment/', views.delete_appointment.as_view(), name='delete_appointment'),
    path('api/edit_appointment/', views.edit_appointment.as_view(), name='edit_appointment'),

    
    path('api/delete_equipment/', views.delete_equipment.as_view(), name='delete_equipment'),
    path('api/edit_equipment/', views.edit_equipment.as_view(), name='edit_equipment'),

    path('api/delete_laboratory/', views.delete_laboratory.as_view(), name='delete_laboratory'),
    path('api/edit_laboratory/', views.edit_laboratory.as_view(), name='edit_laboratory'),

    path('api/delete_Medicalrecord/', views.delete_Medicalrecord.as_view(), name='delete_Medicalrecord'),
    path('api/edit_Medicalrecord/', views.edit_Medicalrecord.as_view(), name='edit_Medicalrecord'),

   

    path('api/delete_patient/', views.delete_patient.as_view(), name='delete_patient'),
    
    path('api/update_patient/', views.update_patient.as_view(), name='update_patient'),

]