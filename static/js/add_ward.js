document.getElementById('addwardForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    
    const PatientID = document.getElementById('patientID').value;
    const DoctorName = document.getElementById('doctorName').value;
    const floorno = document.getElementById('floorno').value;
    const Quantity = document.getElementById('Quantity').value;
    const Avalaibality = document.getElementById('Avalaibality').value;
    
    
    // Basic validation (optional, you can customize this)
    if (!PatientID || !DoctorName || !floorno || !Quantity || !Avalaibality) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        
        PatientID,
        DoctorName,
        floorno,
        Quantity,
        Avalaibality,
    
    });

    // Show success message or redirect
    alert('ward added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
