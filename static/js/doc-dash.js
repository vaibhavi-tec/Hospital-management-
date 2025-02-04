let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editDoctorId').value = row.cells[1].innerText.trim();
    document.getElementById('editName').value = row.cells[2].innerText;
    document.getElementById('editFrom').value = row.cells[3].innerText;
    document.getElementById('editTo').value = row.cells[4].innerText;
    document.getElementById('editMobile').value = row.cells[5].innerText;
    document.getElementById('editPassword').value = row.cells[6].innerText;

   

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    var did = document.getElementById('editDoctorId').value;
    var doctor_name = document.getElementById('editName').value;
    var specialization = document.getElementById('editFrom').value;
    var contact_info = document.getElementById('editTo').value;
    var schedule = document.getElementById('editMobile').value;
    var password = document.getElementById('editPassword').value;

    $.ajax({
        type: "POST",
        url: "/api/edit_doctor/",
        data: {"id":  did, "name":doctor_name,"specialization":specialization ,"contact_info":contact_info ,"schedule":schedule, "password":password},
        success: function(e)
        {
            window.location.replace("/adminsite/docdash");
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
        url: "/api/delete_doctor/",
        data: {"id": id},
        success: function(d)
        {
            window.location.replace("/adminsite/docdash");
        }

    });
}

document.getElementById('filterBtn').addEventListener('click', function() {
    const filterOptions = document.getElementById('filterOptions');
    filterOptions.style.display = filterOptions.style.display === 'none' ? 'block' : 'none';
});

function sortTable(column, order) {
    const table = document.getElementById("doctorTable");
    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));

    // Define column indices for sorting
    const columnIndex = {
        'name': 1,  // Patient Name
        'date': 3   // Date of Appointment
    }[column];

    rows.sort((a, b) => {
        let valA, valB;

        // Extract values for comparison
        if (column === 'date') {
            // Convert date strings to Date objects for comparison
            valA = new Date(a.cells[columnIndex].innerText);
            valB = new Date(b.cells[columnIndex].innerText);
        } else {
            // For text-based sorting
            valA = a.cells[columnIndex].innerText.trim().toLowerCase();
            valB = b.cells[columnIndex].innerText.trim().toLowerCase();
        }

        if (order === 'asc') {
            if (valA < valB) return -1;
            if (valA > valB) return 1;
            return 0;
        } else {
            if (valA < valB) return 1;
            if (valA > valB) return -1;
            return 0;
        }
    });

    // Re-append sorted rows to the table body
    rows.forEach(row => tbody.appendChild(row));
}


