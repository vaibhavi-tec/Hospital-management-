from django.urls import path

from . import views

urlpatterns = [
    path("Staff/", views.Staff, name="Staff"),
    path('Staff/appostaff', views.appostaff, name='appostaff'),
    path('Staff/userdash', views.userdash, name='userdash'),
    path('Staff/inventstaff', views.inventstaff, name='inventstaff'),
    path('Staff/Labdash', views.Labdash, name='Labdash'),
    path('Staff/Equipdash', views.Equipdash, name='Equipdash'),
    path('Staff/Meddash', views.Meddash, name='Meddash'),
    path('Staff/beddash', views.beddash, name='beddash'),
    path('Staff/warddash', views.warddash, name='warddash'),
    path('Staff/patientdash', views.patientdash, name="patientdash"),
    path('Staff/paydash', views.paydash, name="paydash"),
    path("Staff/pharmdash", views.pharmdash, name="pharmdash"),


    path('Staff/addappo', views.addappo, name='addappo'),
    path('Staff/adduserdash', views.adduserdash, name='adduserdash'),
    path('Staff/addin', views.addin, name='addin'),
    path('Staff/addlab', views.addlab, name='addlab'),
    path('Staff/addmed', views.addmed, name='addmed'),
    path('Staff/addequip', views.addequip, name='addequip'),
    path('Staff/addward', views.addward, name='addward'),
    path('Staff/addbed', views.addbed, name='addbed'),
    path('Staff/addpat/', views.addpat, name="addpat"),
     path('Staff/addpay/', views.addpay, name="addpay"),
    path("Staff/addpharm", views.addpharm, name="addpharm"),

    path('api/add_appointment/', views.AddAppointmentView.as_view(), name='add_appointment'),  # API endpoint
    path('api/add_inventory/', views.AddInventoryView.as_view(), name='add_inventory'),
    path('api/add_user/', views.AddUserView.as_view(), name='add_user'),
    path('api/add_lab/', views.AddLabView.as_view(), name='add_lab'),
    path('api/add_equip/', views.AddEquipView.as_view(), name='add_equip'),
    path('api/add_med/', views.AddMedView.as_view(), name='add_med'),
    path('api/add_ward/', views.AddWardView.as_view(), name='add_ward'),
    path('api/add_bed/', views.AddBedView.as_view(), name='add_bed'),
    path('api/addpat/', views.AddPatientView.as_view(), name='add_pat'),
    path('api/addpay/', views.AddPaymentView.as_view(), name='add_pay') ,
    path('api/add_pharm',views.AddPharmacyView.as_view() ,name='add_pharm'),


    path('Staff/invoice', views.invoice, name='invoice'),
    path('Staff/report', views.report, name='report'),


    path('api/delete_appointment/', views.delete_appointment.as_view(), name='delete_appointment'),
    path('api/edit_appointment/', views.edit_appointment.as_view(), name='edit_appointment'),

    path('api/delete_user/', views.delete_user.as_view(), name='delete_user'),
    path('api/edit_user/', views.edit_user.as_view(), name='edit_user'),
    
    path('api/delete_inventory/', views.delete_inventory.as_view(), name='delete_inventory'),
    path('api/edit_inventory/', views.edit_inventory.as_view(), name='edit_inventory'),
    
    path('api/delete_equipment/', views.delete_equipment.as_view(), name='delete_equipment'),
    path('api/edit_equipment/', views.edit_equipment.as_view(), name='edit_equipment'),

    path('api/delete_laboratory/', views.delete_laboratory.as_view(), name='delete_laboratory'),
    path('api/edit_laboratory/', views.edit_laboratory.as_view(), name='edit_laboratory'),

    path('api/delete_Medicalrecord/', views.delete_Medicalrecord.as_view(), name='delete_Medicalrecord'),
    path('api/edit_Medicalrecord/', views.edit_Medicalrecord.as_view(), name='edit_Medicalrecord'),

    path('api/delete_ward/', views.delete_ward.as_view(), name='delete_ward'),
    path('api/update_ward/', views.update_ward.as_view(), name='update_ward'),

    path('api/delete_bed/', views.delete_bed.as_view(), name='delete_bed'),
    path('api/update_bed/', views.update_bed.as_view(), name='update_bed'),

    path('api/delete_patient/', views.delete_patient.as_view(), name='delete_patient'),
    path('api/delete_payment/', views.delete_payment.as_view(), name='delete_payment'),
    
    path('api/update_patient/', views.update_patient.as_view(), name='update_patient'),
    path('api/update_payment/', views.update_payment.as_view(), name='update_payment'),

    

]   