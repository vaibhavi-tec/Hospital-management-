let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('StaffName').value = row.cells[1].innerText;
    document.getElementById('sid').value = row.cells[2].innerText.trim();
    document.getElementById('Specialization').value = row.cells[3].innerText;
    document.getElementById('editMobile').value = row.cells[4].innerText;
    document.getElementById('editPassword').value = row.cells[5].innerText;
    document.getElementById('shift_schedule').value = row.cells[6].innerText;

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    var sname = document.getElementById('StaffName').value;
    var sid = document.getElementById('sid').value;
    var role = document.getElementById('Specialization').value;
    var contact = document.getElementById('editMobile').value;
    var password = document.getElementById('editPassword').value;
    var shift_schedule = document.getElementById('shift_schedule').value;
    

    $.ajax({
        type: "POST",
        url: "/api/edit_staff/",
        data: {"id":  sid, "sname":sname,"role":role, "contact":contact ,"password":password,"shift_schedule":shift_schedule},
        success: function(e)
        {
            window.location.replace("/index/staffdash");
        }

    });
    if (!currentRow) return; 
    // Close the popup
    closeEditPopup();
}

function closeEditPopup() {
    document.getElementById('editPopup').style.display = 'none';
}


   
function deleteRow(id) {
    // Remove the row from the table
    console.log("id: ",id);
    $.ajax({
        type: "POST",
        url: "/api/delete_staff/",
        data: {"id": id},
        success: function(d)
        {
            window.location.replace("/index/staffdash");
        }

    })
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

