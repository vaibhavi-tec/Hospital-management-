document.getElementById('addDoctorForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const Doctorid = document.getElementById('Doctorid').value;
    const DoctorName = document.getElementById('DoctorName').value;
    const specialization = document.getElementById('specialization').value;
    const contact = document.getElementById('contact').value;
    const schedule = document.getElementById('schedule').value;
    const password = document.getElementById('password').value;

    // Basic validation (optional, you can customize this)
    if (!Doctorid ||!DoctorName || !specialization || !contact || !schedule || !password ) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        Doctorid,
        DoctorName,
        specialization,
        contact,
        schedule,
        password
    });

    // Show success message or redirect
    alert('doctor  added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
