from django.db import models


class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    appointment_id = models.CharField(primary_key=True, max_length=255, unique=True, blank=True, editable=False)
    appointment_date = models.DateField()
    appointment_from = models.TimeField()
    appointment_to = models.TimeField()
    gender = models.CharField(max_length=10)
    doctor_name = models.CharField(max_length=10)
    condition = models.TextField()

    def save(self, *args, **kwargs):
        if not self.appointment_id:
            last_appointment = Appointment.objects.all().order_by('-appointment_id').first()
            if last_appointment:
                last_id = int(last_appointment.appointment_id[2:])
                new_id = f"AP{last_id + 1:02d}"
            else:
                new_id = "AP00"
            self.appointment_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Appointment ID: {self.appointment_id} - {self.patient_name}"


class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    inventory_id = models.CharField(primary_key=True, max_length=255, unique=True, blank=True, editable=False)
    quantity = models.CharField(max_length=255)  
    supplier = models.CharField(max_length=100)
    cost = models.IntegerField()
    stock_level = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        if not self.inventory_id:
            last_inventory = Inventory.objects.all().order_by('-inventory_id').first()
            if last_inventory:
                last_id = int(last_inventory.inventory_id[2:])
                new_id = f"IN{last_id + 1:02d}"
            else:
                new_id = "IN00"
            self.inventory_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Inventory ID: {self.inventory_id} - {self.item_name}"
    
class User(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=True , default="Patient")
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=255)  



class Lab(models.Model):
        patient_name = models.TextField()
        laboratory_test = models.CharField(max_length=20, editable=False)
        laboratory_ID=models.CharField(max_length=255, unique=True, blank=True,editable=False)
        cost_of_service = models.DecimalField(max_digits=10, decimal_places=2)
        ref_doctor = models.TextField()
       

        
        def save(self, *args, **kwargs):
            if not self.laboratory_ID:
                # Generate appointment ID
                last_lab = Lab.objects.all().order_by('-id').first()
                if last_lab:
                    last_id = int(last_lab.laboratory_ID[2:])  # Extract number part
                    new_id = f"LA{last_id + 1:02d}"
                else:
                    new_id = "LA00"
                self.laboratory_ID = new_id
            super().save(*args, **kwargs)
        def _str_(self):
            return f"{self.laboratory_test} for Patient {self.patient_id} by {self.reference_doctor}"

class Equip(models.Model):
        equipment_id = models.CharField(max_length=255, unique=True, blank=True,editable=False)
        equipment_name = models.CharField(max_length=100,editable=False)
        equipment_status = models.CharField(max_length=20)
            
        def save(self, *args, **kwargs):
            if not self.equipment_id:
                # Generate appointment ID
                last_equip = Equip.objects.all().order_by('-id').first()
                if last_equip:
                    last_id = int(last_equip.equipment_id[2:])  # Extract number part
                    new_id = f"EQ{last_id + 1:02d}"
                else:
                    new_id = "EQ00"
                self.equipment_id = new_id
            super().save(*args, **kwargs)
    
class Med(models.Model):
        record_id = models.CharField(max_length=255, blank=True,editable=False)
        patient_id = models.TextField(max_length=255, blank=True,editable=False)
        doctor_id = models.TextField(max_length=255, blank=True,editable=False)
        diagnosis= models.TextField(max_length=100,editable=False)
        treatment= models.TextField(max_length=100,editable=False)
        prescriptions=models.TextField(max_length=100,editable=False)
        test_results=models.TextField(max_length=20)

            
        def save(self, *args, **kwargs):
            if not self.record_id:
                # Generate appointment ID
                last_med = Med.objects.all().order_by('-id').first()
                if last_med:
                    last_id = int(last_med.record_id[2:])  # Extract number part
                    new_id = f"MR{last_id + 1:02d}"
                else:
                    new_id = "MR00"
                self.record_id = new_id
            super().save(*args, **kwargs)



class Ward(models.Model):
    ward_id = models.CharField(primary_key=True, max_length=120)
    patient_id = models.CharField(max_length=120)
      # This field is not nullable
    doctor_name = models.CharField(max_length=120)
    floor_no = models.IntegerField()
    quantity = models.IntegerField()
    availability = models.CharField(default=True, max_length=120)

    def save(self, *args, **kwargs):
            if not self.ward_id:
                last_ward = Ward.objects.all().order_by('-ward_id').first()
                if last_ward:
                    last_id = int(last_ward.ward_id[2:])
                    new_id = f"WA{last_id + 1:02d}"
                else:
                    new_id = "WA00"
                self.ward_id = new_id
            super().save(*args, **kwargs)


        
        

class Bed(models.Model):
        bed_id = models.CharField(primary_key=True , max_length=120)
        date = models.DateField()
        ward_id = models.CharField(max_length=120)
        patient_name = models.CharField(max_length=120)
        doctor_name = models.CharField(max_length=120)
        Patient_Status = models.CharField(max_length=120)
        Prescription = models.CharField(max_length=120)

        def save(self, *args, **kwargs):
            if not self.bed_id:
                last_bed = Bed.objects.all().order_by('-bed_id').first()
                if last_bed:
                    last_id = int(last_bed.bed_id[2:])
                    new_id = f"BE{last_id + 1:02d}"
                else:
                    new_id = "BE00"
                self.bed_id = new_id
            super().save(*args, **kwargs)

        

from .storage import StaticStorage

class Patient(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=10)
    patient_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    medical_history = models.FileField(storage=StaticStorage(), null=True, blank=True)
    address = models.TextField()
    status = models.CharField(max_length=20)
    patientpassword = models.CharField(max_length=100)


    def save(self, *args, **kwargs):
        if not self.patient_id:
            last_patient = Patient.objects.all().order_by('-patient_id').first()
            if last_patient:
                last_id = int(last_patient.patient_id[2:])
                new_id = f"PA{last_id + 1:02d}"
            else:
                new_id = "PA00"
            self.patient_id = new_id
        super().save(*args, **kwargs)
    

class Payment(models.Model):

    payment_id = models.CharField(primary_key=True, max_length=10)   
    patient_name = models.CharField(max_length=100)
    appointment_id = models.CharField( max_length=10)
    date = models.DateField()
    status = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.payment_id:
            last_payment = Payment.objects.all().order_by('-payment_id').first()
            if last_payment:
                last_id = int(last_payment.payment_id[2:])
                new_id = f"PY{last_id + 1:02d}"
            else:
                new_id = "PY00"
            self.payment_id = new_id
        super().save(*args, **kwargs)


class Doctor(models.Model):
       doctor_id = models.CharField(max_length=100, unique=True ,null=False)
       doctor_name = models.CharField(max_length=100)
       specialization = models.CharField(max_length=100)
       contact_info = models.CharField(max_length=100, blank=True, null=True)
       schedule = models.TextField(max_length=100,blank=True, null=True)
       password = models.CharField(max_length=128) 

       def save(self, *args, **kwargs):
            if not self.doctor_id:
                # Generate Doctor ID
                last_doc = Doctor.objects.all().order_by('-id').first()
                if last_doc:
                    last_id = int(last_doc.doctor_id[2:])  # Extract number part
                    new_id = f"DO{last_id + 1:02d}"
                else:
                    new_id = "DO00"
                self.doctor_id = new_id
            super().save(*args, **kwargs)   


class Pharmacy(models.Model):
    pharmacy_id = models.CharField(max_length=100, unique=True, null=False)
    drug_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()
    supplier = models.CharField(max_length=100, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
 # Default value added here

    def save(self, *args, **kwargs):
            if not self.pharmacy_id:
                # Generate Pharmacy ID
                last_pharm = Pharmacy.objects.all().order_by('-id').first()
                if last_pharm:
                    last_id = int(last_pharm.pharmacy_id[2:])  # Extract number part
                    new_id = f"PH{last_id + 1:02d}"
                else:
                    new_id = "PH00"
                self.pharmacy_id = new_id
            super().save(*args, **kwargs)



class Staff(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=120)
    fullname = models.CharField(max_length=100, default='')
    specialization = models.CharField(max_length=50, default='dentist')
    # role = models.CharField(max_length=10)
    contact_information = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, default='1234')
    shift_schedule = models.TextField(blank=True, null=True)

 
   
    def save(self, *args, **kwargs):
            if not self.staff_id:
                # Generate Pharmacy ID
                last_staff = Staff.objects.all().order_by('-staff_id').first()
                if last_staff:
                    last_id = int(last_staff.staff_id[2:])  # Extract number part
                    new_id = f"ST{last_id + 1:02d}"
                else:
                    new_id = "ST00"
                self.staff_id = new_id
            super().save(*args, **kwargs)


    def __str__(self):
        return self.full_name 