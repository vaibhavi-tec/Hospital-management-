document.getElementById('addPayForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const patientid = document.getElementById('patientid').value;
    const patientname = document.getElementById('patientname').value;
    const appointmentid = document.getElementById('appointmentid').value;
    const date = document.getElementById('date').value;
    const status = document.getElementById('status').value;
    const amount = document.getElementById('amount').value;


    // Basic validation (optional, you can customize this)
    if (!patientid || !patientname || !appointmentid || !date || !status || !amount) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        patientid,
        patientname,
        appointmentid,
        date,
        status,
        amount,
    });

    // Show success message or redirect
    alert('Appointment added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
