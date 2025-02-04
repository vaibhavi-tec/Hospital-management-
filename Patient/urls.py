from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("afterhome", views.afterhome, name="afterhome"),
    path('about', views.about, name='about'),
    path('appointment', views.appointment, name='appointment'),
    path('api/add_appointment/', views.AddAppointmentView.as_view(), name='add_appointment'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('setpass', views.setpass, name='setpass'),
    path('trysign', views.trysign, name='trysign'),
    path('signin', views.signin, name='signin'),
    path('view_patient', views.view_patient, name='view_patient'),
    path('login_check/', views.login_view.as_view(), name='login_check'),
    path('create_staff', views.create_staff.as_view(), name='create_staff'),
    path('view_staff', views.view_staff.as_view(), name='view_staff'),
    path('delete_employee', views.delete_employee.as_view(), name='delete_employee'),
    path('UserProfileView', views.UserProfileView.as_view(), name='UserProfileView'),
    path('api/addpat/', views.AddPatientView.as_view(), name='add_pat'),
    path('api/add_user/', views.AddUserView.as_view(), name='add_user'),
    path('UserDoctorView', views.UserDoctorView.as_view(), name='UserDoctorView'),
]