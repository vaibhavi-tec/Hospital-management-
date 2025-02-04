from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from Adminsite.models import Appointment, Lab, Med, Equip,Patient

def doctor(request):
    context["currentuser"] = self.request.session.get("userdata")
    return render(request,"doctor/doctorindex.html/",context)
# Create your views here.

def appostaff(request):
    appointments = Appointment.objects.all()
    return render(request,"doctor/Appointment-doctor.html/", {"userdata": appointments})

def Labdash(request):
    lab=Lab.objects.all()
    return render(request,'doctor/Lab-doctor.html',{"userdata":lab})
    


def Equipdash(request):
    equip=Equip.objects.all()
    return render(request,"doctor/Equip-doctor.html" , {"userdata":equip})

def Meddash(request):
    med=Med.objects.all()
    return render(request,'doctor/Med-doctor.html',{"userdata":med})

def patientdash(request):
     # return HttpResponse("Hello, world. You're at the polls index.")
      patient = Patient.objects.all()
    # Pass the inventory items to the template
      return render(request, "doctor/pat-doctor.html", {"userdata": patient})

# Add forms ..................................................ADD FORMS.........................................

def addappo(request):
    return render(request,"doctor/add_appodash-doctor.html/",context=None)

def addlab(request):
    return render(request,'doctor/add_lab-doctor.html',context=None)

def report(request):
    return render(request,'doctor/repoinvoice-doctor.html',context=None)

def addmed(request):
    return render(request,'doctor/add_med-doctor.html',context=None)

def addequip(request):
    return render(request,'doctor/add_equip-doctor.html',context=None)

def addpat(request):
    return render(request,"doctor/addpat-doctor.html",context=None)


#.........APPOINTMENT ..................................... ADD  /UPDATE / DELETE FORMS................................


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

class delete_appointment(APIView):
        def post(self,request):
            id = request.POST['id']
            Appointment.objects.filter(appointment_id=id).delete()
            return JsonResponse({"status":"pass"})

class edit_appointment(APIView):
    def post(self,request):
        id = request.POST['id']
        patient_name = request.POST['name']
        # appointment_date = request.POST['appointment_date']
        # appointment_from = request.POST['fromtime']
        # appointment_to = request.POST['totime']
        gender = request.POST['gender']
        doctor_name = request.POST['doctor']
        condition = request.POST['condition']
        Appointment.objects.filter(appointment_id = id).update(patient_name=patient_name)
        Appointment.objects.filter(appointment_id = id).update(gender=gender)
        Appointment.objects.filter(appointment_id = id).update(doctor_name=doctor_name)
        Appointment.objects.filter(appointment_id = id).update(condition=condition)
        return JsonResponse({"status":"pass"})
    

#.........LABORATORY ..................................... ADD  /UPDATE / DELETE FORMS................................

class AddLabView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        lab = Lab(
            patient_name=data.get('patientName'),
            # appointment_id is not set here, Django will auto-generate it
            laboratory_test=data.get('labTest'),
            # laboratory_ID=data.get('labID'),
            cost_of_service=data.get('cost'),
            ref_doctor=data.get('refDoctor'),
        )
        lab.save()
        # Return a success message
        return JsonResponse({"message": "Laboratory added successfully!"})
    
class delete_laboratory(APIView):
        def post(self,request):
            id = request.POST['id']
            Lab.objects.filter(laboratory_ID=id).delete()
            return JsonResponse({"status":"pass"})

class edit_laboratory(APIView):
    def post(self,request):
        id = request.POST['id']
        laboratory_test = request.POST['labtest']
        cost_of_service = request.POST['labcost']
        ref_doctor = request.POST['rdoctor']
        Lab.objects.filter( laboratory_ID = id).update(laboratory_test=laboratory_test)
        Lab.objects.filter( laboratory_ID = id).update(cost_of_service=cost_of_service)
        Lab.objects.filter( laboratory_ID = id).update(ref_doctor=ref_doctor)
        return JsonResponse({"status":"pass"})


#.........EQUIPMENT ..................................... ADD  /UPDATE / DELETE FORMS................................

class AddEquipView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        equip = Equip(
            equipment_name=data.get('editName'),
            # appointment_id is not set here, Django will auto-generate it
            equipment_status=data.get('editStatus'),
            # laboratory_ID=data.get('labID'),
        )
        equip.save()
        # Return a success message
        return JsonResponse({"message": "Equipment added successfully!"})
    
class delete_equipment(APIView):
        def post(self,request):
            id = request.POST['id']
            Equip.objects.filter(equipment_id=id).delete()
            return JsonResponse({"status":"pass"})

class edit_equipment(APIView):
    def post(self,request):
        id = request.POST['id']
        equipment_name = request.POST['name']
        # appointment_date = request.POST['appointment_date']
        # appointment_from = request.POST['fromtime']
        # appointment_to = request.POST['totime']
        equipment_status = request.POST['status']
       
        Equip.objects.filter(equipment_id = id).update(equipment_name=equipment_name)
        Equip.objects.filter(equipment_id = id).update(equipment_status=equipment_status)
      
        return JsonResponse({"status":"pass"})

#.........MEDICAL RECORD ..................................... ADD  /UPDATE / DELETE FORMS................................


class AddMedView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        med = Med(
            patient_id=data.get('patient_id'),
            doctor_id=data.get('doctor_id'),
            diagnosis=data.get('diagnosis'),
            # appointment_id is not set here, Django will auto-generate it
            treatment=data.get('treatment'),
            prescriptions=data.get('prescriptions'),
            test_results=data.get('testResults'),
        )
        med.save()
        # Return a success message
        return JsonResponse({"message": "Medical Record added successfully!"})
    
   
class delete_Medicalrecord(APIView):
        def post(self,request):
            id = request.POST['id']
            Med.objects.filter(record_id=id).delete()
            return JsonResponse({"status":"pass"})

class edit_Medicalrecord(APIView):
    def post(self,request):
        id = request.POST['id']
        patientid = request.POST['patid']
        doctorid = request.POST['docid']
        diag = request.POST['dia']
        treat = request.POST['treating']
        pres = request.POST['prescrip']
        testresult= request.POST['testres']
        Med.objects.filter( record_id = id).update(patient_id=patientid)
        Med.objects.filter( record_id = id).update(doctor_id=doctorid)
        Med.objects.filter( record_id = id).update(diagnosis=diag)
        Med.objects.filter( record_id = id).update(treatment=treat)
        Med.objects.filter( record_id = id).update(prescriptions=pres)
        Med.objects.filter( record_id = id).update(test_results=testresult)
        return JsonResponse({"status":"pass"})

#.........PATIENT ..................................... ADD  /UPDATE / DELETE FORMS................................


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
    
class delete_patient(APIView):
        def post(self,request):
            id = request.POST['id']
            Patient.objects.filter(patient_id=id).delete()
            return JsonResponse({"status":"pass"})

class update_patient(APIView):
    def post(self,request):
        id = request.POST['id']
        patientname = request.POST['name']
        # appointment_date = request.POST['appointment_date']
        # appointment_from = request.POST['fromtime']
        # appointment_to = request.POST['totime']
        phonenumber = request.POST['number']
        gender = request.POST['gender']
        date = request.POST['dateofbirth']
        medicalhistory = request.POST['medicalhistory']
        address = request.POST['address']
        status = request.POST['status']
        Patient.objects.filter(patient_id = id).update(patient_name=patientname)
        Patient.objects.filter(patient_id = id).update(phone_number=phonenumber)
        Patient.objects.filter(patient_id = id).update(gender=gender)
        Patient.objects.filter(patient_id = id).update(date_of_birth=date)
        Patient.objects.filter(patient_id = id).update(medical_history=medicalhistory)
        Patient.objects.filter(patient_id = id).update(address=address)
        Patient.objects.filter(patient_id = id).update(status=status)
        return JsonResponse({"status":"pass"})
