document.getElementById('addAppointmentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    
    const diagnosis = document.getElementById('diagnosis').value;
    const treatment = document.getElementById('treatment').value;
    const prescriptions = document.getElementById('prescriptions').value;
    const testResults = document.getElementById('testResults').value;

    // Basic validation (optional, you can customize this)
    if (!diagnosis || !treatment || !prescriptions || !testResults ) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        diagnosis,
        treatment,
        prescriptions,
        testResults

    });

    // Show success message or redirect
    alert('Medical Record service added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
