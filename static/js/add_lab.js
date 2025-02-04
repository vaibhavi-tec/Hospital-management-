document.getElementById('addAppointmentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const patientName = document.getElementById('patientName').value;
   
    const labTest = document.getElementById('labTest').value;
    const cost = document.getElementById('cost').value;
    const refDoctor = document.getElementById('refDoctor').value;

    // Basic validation (optional, you can customize this)
    if (!patientName || !labTest || !cost || !refDoctor ) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        patientName,
        labTest,
        cost,
        refDoctor
    });

    // Show success message or redirect
    alert('Lab service added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
