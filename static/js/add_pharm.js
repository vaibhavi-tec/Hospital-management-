document.getElementById('addPharmacyForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    
    const DrugName = document.getElementById('DrugName').value;
    const quantity = document.getElementById('quantity').value;
    const expairy_date = document.getElementById('expairy_date').value;
    const Supplier = document.getElementById('Supplier').value;
    const Cost = document.getElementById('Cost').value;

    // Basic validation (optional, you can customize this)
    if (!DrugName || !quantity || !expairy_date || !Supplier || !Cost) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
       
        DrugName,
        quantity,
        expairy_date,
        Supplier,
        Cost
    });

    // Show success message or redirect
    alert('Medicine  added successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
