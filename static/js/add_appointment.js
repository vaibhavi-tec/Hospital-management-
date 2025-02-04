document.getElementById('addAppointmentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const patientName = document.getElementById('patientName').value;
    const appointmentID = document.getElementById('appointmentID').value;
    const appointmentDate = document.getElementById('appointmentDate').value;
    const appointmentFrom = document.getElementById('appointmentFrom').value;
    const appointmentTo = document.getElementById('appointmentTo').value;
    const gender = document.getElementById('gender').value;
    const doctorName = document.getElementById('doctorName').value;
    const condition = document.getElementById('condition').value;

    // Basic validation (optional, you can customize this)
    if (!patientName || !appointmentID || !appointmentDate || !appointmentFrom || !appointmentTo || !gender || !doctorName || !condition) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        patientName,
        appointmentID,
        appointmentDate,
        appointmentFrom,
        appointmentTo,
        gender,
        doctorName,
        condition
    });

    // Show success message or redirect
    alert('Appointment added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
