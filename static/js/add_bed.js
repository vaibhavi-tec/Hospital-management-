document.getElementById('addbedForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    
    const wardID = document.getElementById('wardID').value;
    const Date = document.getElementById('Date').value;
    const doctorName = document.getElementById('doctorName').value;
    const patientname = document.getElementById('patientname').value;
    const patientstatus = document.getElementById('patientstatus').value;
    const prescription = document.getElementById('prescription').value;
    
    
    // Basic validation (optional, you can customize this)
    if (!wardID || !Date || !doctorName || !patientname || !patientstatus || !prescription) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        
        wardID,
        Date,
        doctorName,
        patientname,
        patientstatus,
        prescription,
    
    });

    // Show success message or redirect
    alert('bed added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
