document.getElementById('addStaffForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    
    const StaffName = document.getElementById('StaffName').value;
    const editFrom = document.getElementById('editFrom').value;
    const editTo = document.getElementById('editTo').value;
    const editMobile = document.getElementById('editMobile').value;
    const editPassword = document.getElementById('editPassword').value;
   

    // Basic validation (optional, you can customize this)
    if (!StaffName|| !editFrom || !editTo || !editMobile || !editPassword ) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        
        StaffName,
        editFrom,
        editTo,
        editMobile,
        editPassword

    });

    // Show success message or redirect
    alert('Staff added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
