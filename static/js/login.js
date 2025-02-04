document.getElementById('addsignupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const patientName = document.getElementById('patientName').value;
    const patientphone = document.getElementById('patientphone').value;
    const patientgender = document.getElementById('patientgender').value;
    const dob = document.getElementById('dob').value;
    const medicalhistory = document.getElementById('medicalhistory').value;
    const address = document.getElementById('address').value;
    const password = document.getElementById('password').value;

    // Basic validation (optional, you can customize this)
    if (!patientName || !patientphone || !patientgender || !dob || !medicalhistory || !address || !password) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        patientName,
        patientphone,
        patientgender,
        dob,
        medicalhistory,
        address,
        password
    });

    // Show success message or redirect
    alert(' Signup  successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
