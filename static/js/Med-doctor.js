let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('recordID').value = row.cells[1].innerText.trim();
    document.getElementById('patientID').value = row.cells[2].innerText;
    document.getElementById('doctorID').value = row.cells[3].innerText;
    document.getElementById('diagnosis').value = row.cells[4].innerText;
    document.getElementById('treatment').value = row.cells[5].innerText;
    document.getElementById('prescriptions').value = row.cells[6].innerText;
    document.getElementById('testResults').value = row.cells[7].innerText;

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    var recordid = document.getElementById('recordID').value;
    var patientid = document.getElementById('patientID').value;
    var doctorid= document.getElementById('doctorID').value;
    var diag = document.getElementById('diagnosis').value;
    var treat = document.getElementById('treatment').value;
    var pres = document.getElementById('prescriptions').value;
    var testresult = document.getElementById('testResults').value;

    $.ajax({
        type: "POST",
        url: "/api/edit_Medicalrecord/",
        data: {"id": recordid, "patid": patientid,"docid" : doctorid ,"dia" : diag ,"treating" : treat ,"prescrip" :pres ,"testres":testresult},
        success: function(e)
        {
            window.location.replace("/Doctor/doctor/Meddash");
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

    
    console.log("id:",id);
    $.ajax({
        type: "POST",
        url: "/api/delete_Medicalrecord/",
        data: {"id": id},
        success: function(d)
        {
            window.location.replace("/Doctor/doctor/Meddash");
        }

    });
}


document.getElementById('filterBtn').addEventListener('click', function() {
    const filterOptions = document.getElementById('filterOptions');
    filterOptions.style.display = filterOptions.style.display === 'none' ? 'block' : 'none';
});

function sortTable(column, order) {
    const table = document.getElementById("medTable");
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

    rows.forEach(row => tbody.appendChild(row));
}
