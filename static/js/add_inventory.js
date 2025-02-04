document.getElementById('addInventoryForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const itemName = document.getElementById('itemName').value;
    const quantity = document.getElementById('quantity').value;
    const supplier = document.getElementById('supplier').value;
    const cost = document.getElementById('cost').value;
    const stockLevel = document.getElementById('stockLevel').value;

    // Basic validation
    if (!itemName || !quantity || !supplier || !cost || !stockLevel) {
        alert('Please fill in all fields.');
        return;
    }

    // Send data to server or handle it here
    console.log({
        itemName,
        quantity,
        supplier,
        cost,
        stockLevel
    });

    alert('Inventory item added successfully!');
});
