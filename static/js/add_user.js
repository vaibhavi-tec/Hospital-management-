document.getElementById('addUserForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const UserName = document.getElementById('UserName').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    // Basic validation (optional, you can customize this)
    if (!UserName || !password || !role) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        UserName,
        password,
        role
    });

    // Show success message or redirect
    alert('User added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
