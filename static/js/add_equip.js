document.getElementById('addAppointmentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    
    const editName = document.getElementById('editName').value;
    const editStatus = document.getElementById('editStatus').value;
 

    // Basic validation (optional, you can customize this)
    if (!editName || !editStatus ) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        editStatus,
        editName
        
    });

    // Show success message or redirect
    alert('Lab Equipment added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
