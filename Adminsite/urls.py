from django.urls import path
from . import views

urlpatterns = [
    path("adminsite/", views.index, name="index"),


    path('adminsite/appodash', views.appodash, name='appodash'),
    path('adminsite/userdash', views.userdash, name='userdash'),
    path('adminsite/inventdash', views.inventdash, name='inventdash'),
    path('adminsite/Labdash', views.Labdash, name='Labdash'),
    path('adminsite/Equipdash', views.Equipdash, name='Equipdash'),
    path('adminsite/Meddash', views.Meddash, name='Meddash'),
    path('adminsite/beddash', views.beddash, name='beddash'),
    path('adminsite/warddash', views.warddash, name='warddash'),
    path('adminsite/patientdash', views.patientdash, name="patientdash"),
    path('adminsite/paydash', views.paydash, name="paydash"),
     path("adminsite/docdash", views.docdash, name="docdash"),
    path("adminsite/pharmdash", views.pharmdash, name="pharmdash"),
    path("adminsite/staffdash", views.staffdash, name="staffdash"),
    


    path('adminsite/addappodash', views.addappodash, name='addappodash'),
    path('adminsite/adduserdash', views.adduserdash, name='adduserdash'),
    path('adminsite/addinventdash', views.addinventdash, name='addinventdash'),
    path('adminsite/addlab', views.addlab, name='addlab'),
    path('adminsite/addmed', views.addmed, name='addmed'),
    path('adminsite/addequip', views.addequip, name='addequip'),
    path('adminsite/addward', views.addward, name='addward'),
    path('adminsite/addbed', views.addbed, name='addbed'),
    path('adminsite/addpat/', views.addpat, name="addpat"),
     path('adminsite/addpay/', views.addpay, name="addpay"),
     path("adminsite/adddoc", views.adddoc, name="adddoc"),
    path("adminsite/addpharm", views.addpharm, name="addpharm"),
    path("adminsite/addstaff/", views.addstaff, name="addstaff"),




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
    path('api/add_doc',views.AddDoctorView.as_view() ,name='add_doc'),
    path('api/add_pharm',views.AddPharmacyView.as_view() ,name='add_pharm'),
    path('api/add_staff',views.AddStaffView.as_view() ,name='add_staff'),


    path('adminsite/invoice', views.invoice, name='invoice'),
    path('adminsite/report', views.report, name='report'),


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

    path('api/delete_staff/',views.delete_staff.as_view(), name='delete_staff'),
    path('api/edit_staff/', views.edit_staff.as_view(), name='edit_staff'), 

    path('api/delete_doctor/',views.delete_doctor.as_view(), name='delete_doctor'),
    path('api/edit_doctor/', views.edit_doctor.as_view(), name='edit_doctor'),

]
