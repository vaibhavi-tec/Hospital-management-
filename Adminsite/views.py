from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Appointment, Inventory, User, Lab, Med, Equip, Bed, Ward, Patient, Payment,Doctor, Pharmacy, Staff

def index(request):
    return render(request, "admin/index.html")


# dashboard tables........................................................................................

def appodash(request):
    # Fetch all appointments from the database
    appointments = Appointment.objects.all()
    # Pass the appointments to the template
    return render(request, "admin/Appointment-dash.html", {"userdata": appointments})

def inventdash(request):
    # Fetch all inventory items from the database
    inventory = Inventory.objects.all()
    # Pass the inventory items to the template
    return render(request, "admin/invent-dash.html", {"userdata": inventory})


def userdash(request):
    # Fetch all inventory items from the database
    user = User.objects.all()
    # Pass the inventory items to the template
    return render(request, "admin/user-dash.html", {"userdata": user})

def Labdash(request):
    lab=Lab.objects.all()
    return render(request,'admin/Lab-dash.html',{"userdata":lab})
    


def Equipdash(request):
    equip=Equip.objects.all()
    return render(request,"admin/Equipdash.html" , {"userdata":equip})

def Meddash(request):
    med=Med.objects.all()
    return render(request,'admin/Med-dash.html',{"userdata":med})

def beddash(request):
     # return HttpResponse("Hello, world. You're at the polls index.")
      bed = Bed.objects.all()
    # Pass the inventory items to the template
      return render(request, "admin/bed-dash.html", {"userdata": bed})

def warddash(request):
    # Fetch all inventory items from the database
    ward = Ward.objects.all()
    # Pass the inventory items to the template
    return render(request, "admin/ward-dash.html", {"userdata": ward})

def patientdash(request):
     # return HttpResponse("Hello, world. You're at the polls index.")
      patient = Patient.objects.all()
    # Pass the inventory items to the template
      return render(request, "admin/patientdash.html", {"userdata": patient})

def paydash(request):
    # Fetch all inventory items from the database
    payment = Payment.objects.all()
    # Pass the inventory items to the template
    return render(request, "admin/paydash.html", {"userdata": payment})


def docdash(request):
    doctor = Doctor.objects.all()
    return render(request, 'admin/doc-dash.html',{"userdata":doctor})

def pharmdash(request):
    pharmacy = Pharmacy.objects.all()
    return render(request, 'admin/pharm-dash.html',{"userdata":pharmacy})
    
    
def staffdash(request):
    staff = Staff.objects.all()
    return render(request, 'admin/staff-dash.html',{"userdata":staff})

# Add forms ..................................................ADD FORMS.........................................


def addappodash(request):
    return render(request, "admin/add_appodash.html",context=None)

def addinventdash(request):
    return render(request, "admin/add_inventory.html",context=None)

def adduserdash(request):
    return render(request, "admin/add_user.html",context=None)

def invoice(request):
    return render(request, "admin/payinvoice.html",context=None)

def addlab(request):
    return render(request,'admin/add_lab.html',context=None)

def report(request):
    return render(request,'admin/repoinvoice.html',context=None)

def addmed(request):
    return render(request,'admin/add_med.html',context=None)

def addequip(request):
    return render(request,'admin/add_equip.html',context=None)


def addward(request):
     # return HttpResponse("Hello, world. You're at the polls index.")
      return render(request,"admin/add_ward.html", context=None)

def addbed(request):
     # return HttpResponse("Hello, world. You're at the polls index.")
      return render(request,"admin/add_bed.html", context=None)


def addpat(request):
    return render(request,"admin/addpat.html",context=None)

def addpay(request):
    return render(request,"admin/addpay.html",context=None)


def adddoc(request):
    return render(request, 'admin/add_doc.html',context=None)

def addpharm(request):
    return render(request, 'admin/add_pharm.html',context=None)

def addstaff(request):
    return render(request, 'admin/add_staff.html',context=None)

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
    

#.........USER ..................................... ADD  /UPDATE / DELETE FORMS................................


    
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
        return JsonResponse({"message": "Appointment added successfully!"})
    
class delete_user(APIView):
    def post(self,request):
        username = request.POST['username']
        User.objects.filter(username=username).delete()
        return JsonResponse({"status":"pass"})
    
class edit_user(APIView):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        # appointment_date = request.POST['appointment_date']
        # appointment_from = request.POST['fromtime']
        # appointment_to = request.POST['totime']
        role = request.POST['role']
        doctor_name = request.POST['doctor']
        condition = request.POST['condition']
        User.objects.filter(username = username).update(password=password)
        User.objects.filter(username = username).update(role=role)
        return JsonResponse({"status":"pass"})

#.........INVENTORY ..................................... ADD  /UPDATE / DELETE FORMS................................
    
class AddInventoryView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        inventory=Inventory(
            item_name=data.get('itemName'),
            # appointment_id is not set here, Django will auto-generate it
            quantity=data.get('quantity'),
            supplier=data.get('supplier'),
            cost=data.get('cost'),
            stock_level=data.get('stockLevel'),
        )
        inventory.save()
        # Return a success message
        return JsonResponse({"message": "Inventory added successfully!"})

class delete_inventory(APIView):
    def post(self,request):
        id = request.POST['id']
        Inventory.objects.filter(inventory_id=id).delete()
        return JsonResponse({"status":"pass"})


class edit_inventory(APIView):
    def post(self,request):
        id = request.POST['id']
        item_name = request.POST['name']
        quantity = request.POST['quantity']
        supplier = request.POST['supplier']
        cost = request.POST['cost']
        stock_level = request.POST['stock_level']
        Inventory.objects.filter(inventory_id = id).update(item_name=item_name)
        Inventory.objects.filter(inventory_id = id).update(quantity=quantity)
        Inventory.objects.filter(inventory_id = id).update(supplier=supplier)
        Inventory.objects.filter(inventory_id = id).update(cost=cost)
        Inventory.objects.filter(inventory_id = id).update(stock_level=stock_level)
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

    

#.........WARD ..................................... ADD  /UPDATE / DELETE FORMS................................

class AddWardView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        
        ward=Ward(
            
           
            patient_id=data.get('patientID'),
            doctor_name=data.get('doctorName'),
            floor_no =data.get('floorno'),
            quantity =data.get('Quantity'),
            availability =data.get('Avalaibality'),
        )
        ward.save()
       
        return JsonResponse({"message": "ward added successfully!"})

class delete_ward(APIView):
        def post(self,request):
            id = request.POST['id']
            Ward.objects.filter(ward_id=id).delete()
            return JsonResponse({"status":"pass"})

class update_ward(APIView):
    def post(self,request):
        id = request.POST['id']
        pid  = request.POST['Pid'] 
        name  = request.POST['name']
        floor = request.POST['floor']
        quan = request.POST['quan']
        ava = request.POST['ava']
        Ward.objects.filter(ward_id = id).update(patient_id=pid)
        Ward.objects.filter(ward_id = id).update(doctor_name=name)
        Ward.objects.filter(ward_id = id).update(floor_no=floor)
        Ward.objects.filter(ward_id = id).update(quantity=quan)
        Ward.objects.filter(ward_id = id).update(availability=ava)
        return JsonResponse({"status":"pass"})


#.........BED ..................................... ADD  /UPDATE / DELETE FORMS................................

class AddBedView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
       
        bed=Bed(
            
            bed_id=data.get('bedID'),
            date=data.get('Date'),
            ward_id=data.get('wardID'),
            patient_name=data.get('patientname'),
            doctor_name=data.get('doctorName'),
            Patient_Status =data.get('patientstatus'),
            Prescription =data.get('prescription'),
            
        )
        bed.save()
 
        return JsonResponse({"message": "bed added successfully!"})
    
class delete_bed(APIView):
        def post(self,request):
            id = request.POST['id']
            Bed.objects.filter(bed_id=id).delete()
            return JsonResponse({"status":"pass"})

class update_bed(APIView):
    def post(self,request):
        id = request.POST['id']
        wid  = request.POST['wid']
        pname = request.POST['pname']
        dname = request.POST['dname']
        stat = request.POST['stat']
        pre = request.POST['pre']
        Bed.objects.filter(bed_id = id).update(ward_id=wid)
        Bed.objects.filter(bed_id = id).update(patient_name=pname)
        Bed.objects.filter(bed_id = id).update(doctor_name=dname)
        Bed.objects.filter(bed_id = id).update(Patient_Status=stat)
        Bed.objects.filter(bed_id = id).update(Prescription=pre)
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


 #.........PAYMENT ..................................... ADD  /UPDATE / DELETE FORMS................................


class AddPaymentView(APIView):
     def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        payment=Payment(
            
            # appointment_id is not set here, Django will auto-generate it
            patient_name=data.get('patientname'),
            appointment_id=data.get('appointmentid'),
            date=data.get('date'),
            status =data.get('status'),
            amount =data.get('amount'),
        
        )
        
        payment.save()
        # Return a success message
        return JsonResponse({"message": "payment added successfully!"})
     
class delete_payment(APIView):
        def post(self,request):
            id = request.POST['id']
            Payment.objects.filter(payment_id=id).delete()
            return JsonResponse({"status":"pass"})

class update_payment(APIView):
    def post(self,request):
        id = request.POST['id']
        name = request.POST['name']
        # appointment_date = request.POST['appointment_date']
        # appointment_from = request.POST['fromtime']
        # appointment_to = request.POST['totime']
        appointmentid= request.POST['app']
        date = request.POST['date']
        status= request.POST['status']
        amount= request.POST['am']
        Payment.objects.filter(payment_id = id).update(patient_name=name)
        Payment.objects.filter(payment_id = id).update(appointment_id=appointmentid)
        Payment.objects.filter(payment_id = id).update(date=date)
        Payment.objects.filter(payment_id = id).update(status=status)
        Payment.objects.filter(payment_id = id).update(amount=amount)
        return JsonResponse({"status":"pass"})
    
#.........DOCTOR ..................................... ADD  /UPDATE / DELETE FORMS................................

class AddDoctorView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        doctor = Doctor(
            doctor_id=data.get('Doctorid'),
            doctor_name=data.get('DoctorName'),

            # appointment_id is not set here, Django will auto-generate it
            specialization=data.get('specialization'),
            contact_info=data.get('contact'),
            schedule=data.get('schedule'),
            password=data.get('password'),
        )
        
        doctor.save()
        # Return a success message
        return JsonResponse({"message": "Doctor added successfully!"})
    
class delete_doctor(APIView):
    def post(self,request):
            id = request.POST['id']
            Doctor.objects.filter(doctor_id=id).delete()
            return JsonResponse({"status":"pass"})


class edit_doctor(APIView):
    def post(self,request):
        id = request.POST['id']
        doctor_name = request.POST['name']
        # appointment_date = request.POST['appointment_date']
        # appointment_from = request.POST['fromtime']
        # appointment_to = request.POST['totime']
        
        specialization = request.POST['specialization']
        contact_info = request.POST['contact_info']
        schedule = request.POST['schedule']
        password = request.POST['password']
        Doctor.objects.filter(doctor_id = id).update(doctor_name=doctor_name)
        Doctor.objects.filter(doctor_id = id).update(specialization=specialization)
        Doctor.objects.filter(doctor_id = id).update(contact_info=contact_info)
        Doctor.objects.filter(doctor_id = id).update(schedule=schedule)
        Doctor.objects.filter(doctor_id = id).update(password=password)

        return JsonResponse({"status":"pass"})
    
#.........PHARMACY ..................................... ADD  /UPDATE / DELETE FORMS................................

class AddPharmacyView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        pharmacy = Pharmacy(
            pharmacy_id=data.get('pharmacyid'),
            drug_name=data.get('DrugName'),
            quantity=data.get('quantity'),
            expiry_date=data.get('expairy_date'),
            supplier=data.get('supplier'),
            cost=data.get('cost'),
        )
        
        pharmacy.save()
        # Return a success message
        return JsonResponse({"message": "Medicine added successfully!"})
    

#.........STAFF ..................................... ADD  /UPDATE / DELETE FORMS................................
    
class AddStaffView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # Create a new appointment without the appointment_id
        staff = Staff(
            fullname=data.get('StaffName'),
            specialization = data.get('editFrom'),
            contact_information=data.get('editTo'),
            password = data.get('editPassword'),
            shift_schedule = data.get('editMobile')
        )
        staff.save()
        # Return a success message
        return JsonResponse({"message": "Staff added successfully!"})
    
class delete_staff(APIView):
    def post(self,request):
            id = request.POST['id']
            Staff.objects.filter(staff_id=id).delete()
            return JsonResponse({"status":"pass"})


class edit_staff(APIView):
    def post(self,request):
        id = request.POST['id']
        sname = request.POST['sname']
        # appointment_date = request.POST['appointment_date']
        # appointment_from = request.POST['fromtime']
        # appointment_to = request.POST['totime']
        
       
        role = request.POST['role']
        contact = request.POST['contact']
        password = request.POST['password']
        shift_schedule=request.POST['shift_schedule']
        Doctor.objects.filter(doctor_id = id).update(fullname=sname)
        Doctor.objects.filter(doctor_id = id).update(specialization=role)
        Doctor.objects.filter(doctor_id = id).update(contact_information=contact)
        Doctor.objects.filter(doctor_id = id).update(password=password)
        Doctor.objects.filter(doctor_id = id).update(shift_schedule=shift_schedule)

        return JsonResponse({"status":"pass"})
