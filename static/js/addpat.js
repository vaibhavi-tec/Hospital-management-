document.getElementById('addPatForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const patientname = document.getElementById('patientname').value;
    const patientphone = document.getElementById('patientphone').value;
    const patientgender = document.getElementById('patientgender').value;
    const dateofbirth = document.getElementById('dateofbirth').value;
    const medicalhistory = document.getElementById('medicalhistory').value;
    const patientaddress = document.getElementById('patientaddress').value;
    const status = document.getElementById('status').value;
    const patientpassword = document.getElementById('patientpassword').value;


    // Basic validation (optional, you can customize this)
    if (!patientname || !patientphone || !patientgender || !dateofbirth || !medicalhistory || !patientaddress || !status|| !patientpassword ) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        patientname,
        patientphone,
        patientgender,
        dateofbirth,
        medicalhistory,
        patientaddress,
        status,
        patientpassword,
    });

    // Show success message or redirect
    alert('Appointment added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
