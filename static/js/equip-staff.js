let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editID').value = row.cells[1].innerText.trim();
    document.getElementById('editName').value = row.cells[2].innerText;
    document.getElementById('editStatus').value = row.cells[3].innerText;

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    var equipid = document.getElementById('editID').value;
    var equipment_name= document.getElementById('editName').value;
    var equipment_status = document.getElementById('editStatus').value;

    $.ajax({
        type: "POST",
        url: "/api/edit_equipment/",
        data: {"id": equipid, "name": equipment_name,"status" : equipment_status },
        success: function(e)
        {
            window.location.replace("/Staff/Staff/Equipdash");
        }

    });
    if (!currentRow) return; // Prevent saving if no row is selected
    
    // Close the popup
    closeEditPopup();
}

function closeEditPopup() {
    document.getElementById('editPopup').style.display = 'none';
}

function deleteRow(id) {
    // Remove the row from the table
    // const row = button.parentNode.parentNode;
    // row.parentNode.removeChild(row);
    console.log("id: ",id);
    $.ajax({
        type: "POST",
        url: "/api/delete_equipment/",
        data: {"id": id},
        success: function(d)
        {
            window.location.replace("/Staff/Staff/Equipdash");
        }

    });


}

document.getElementById('filterBtn').addEventListener('click', function() {
    const filterOptions = document.getElementById('filterOptions');
    filterOptions.style.display = filterOptions.style.display === 'none' ? 'block' : 'none';
});

function sortTable(column, order) {
    const table = document.getElementById('appointmentsTable').getElementsByTagName('tbody')[0];
    const rows = Array.from(table.rows);

    rows.sort((a, b) => {
        let valA = '';
        let valB = '';

        switch (column) {
            case 'name':
                valA = a.cells[1].innerText.trim().toLowerCase();
                valB = b.cells[1].innerText.trim().toLowerCase();
                break;
            case 'date':
                valA = new Date(a.cells[3].innerText);
                valB = new Date(b.cells[3].innerText);
                break;
        }

        if (order === 'asc') {
            return valA > valB ? 1 : -1;
        } else {
            return valA < valB ? 1 : -1;
        }
    });

    rows.forEach(row => table.appendChild(row));
}

document.getElementById('newAppointmentBtn').addEventListener('click', function() {
    alert("This feature to add a new appointment is under development.");
});

