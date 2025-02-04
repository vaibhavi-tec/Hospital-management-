from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from  Adminsite.models import User, Appointment, Patient
from django.views.generic.base import TemplateView


def home(request):
    #return HttpResponse("Hello, world. You're at the Department index.")
    return render(request,"patient/home.html/",context=None)


def afterhome(request):
    #return HttpResponse("Hello, world. You're at the Department index.")
    return render(request,"patient/afterhome.html/",context=None)

def about(request):
    return render(request,"patient/about.html/",context=None)

def appointment(request):
    return render(request,"patient/appointment.html/",context=None)

def setpass(request):
    return render(request,"patient/setpass.html/",context=None)

class AddAppointmentView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        appointment = Appointment(
            patient_name=data.get('patientName'),
            # appointment_id is not set here, Django will auto-generate it
            appointment_date=data.get('appointmentDate'),
            appointment_from=data.get('appointmentFrom'),
            appointment_to=data.get('appointmentTo'),
            gender=data.get('gender'),
            doctor_name=data.get('doctorName'),
            condition=data.get('condition')
        )
        appointment.save()
        # Return a success message
        return JsonResponse({"message": "Appointment added successfully!"})
    
class AddPatientView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        patient=Patient(
            
            # appointment_id is not set here, Django will auto-generate it
            patient_name=data.get('patientname'),
            phone_number=data.get('patientphone'),
            gender=data.get('patientgender'),
            date_of_birth=data.get('dateofbirth'),
            medical_history=data.get('medicalhistory'),
            address =data.get('patientaddress'),
            status =data.get('status'),
            patientpassword =data.get('patientpassword'),
        
        )

        patient.save()
        # Return a success message
        return JsonResponse({"message": "patient added successfully!"})
    
class AddUserView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        user = User(
            username=data.get('UserName'),
            # appointment_id is not set here, Django will auto-generate it
            password=data.get('password'),
            role=data.get('role')
        )
        user.save()
        # Return a success message
        return JsonResponse({"message": "Signed Up successfully!"})

def signup(request):
    return render(request,"patient/signup.html/",context=None)

def login(request):
    return render(request,"patient/login.html/",context=None)

def trysign(request):
    return render(request,"patient/trysign.html/",context=None)

def signin(request):
    return render(request,"patient/trial.html/",context=None)

def view_patient(request):
    return render(request,"patient/view_patient.html/",context=None)

class login_view(APIView):
    def post(self,request):
        patientname=request.data.get('patientname')
        password=request.data.get('pateintpass')
        pt = User.objects.filter(username=patientname,password=password).values()
        print("********pt: ", pt)
        if len(pt) > 0:
            request.session["userdata"]= pt[0]["username"]
            return JsonResponse({"status":"pass", "user": pt[0]["username"], "role": pt[0]["role"]})
        else:
            return JsonResponse({"status": "fail"})

class UserProfileView(TemplateView):
    model = User
    template_name = "index.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        user = User.objects.get(username=username)
        context['currentuser'] = user.username
        return context
    

class UserDoctorView(TemplateView):
    model = User
    template_name = "doctorindex.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        user = User.objects.get(username=username)
        context['currentuser'] = user.username
        return context


  

class create_staff(APIView):
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        utype=request.POST['utype']
        emp=employee()
        
        emp.username=username
        emp.password=password
        emp.utype=utype
        emp.save()
        return JsonResponse({"status": "pass"})
    

class view_staff(TemplateView):
    template_name = 'view_patient.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        userdata=employee.objects.all()
        context['userdata'] = userdata
        return context

class delete_employee(APIView):
    def post(self,request):
        username = request.POST['username']
        employee.objects.filter(username=username).delete()
        return JsonResponse({"status":"pass"})


