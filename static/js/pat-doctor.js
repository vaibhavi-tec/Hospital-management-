let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editID').value = row.cells[1].innerText.trim();
    document.getElementById('editName').value = row.cells[2].innerText.trim();
    document.getElementById('editPhoneNumber').value = row.cells[3].innerText;
    document.getElementById('editGender').value = row.cells[4].innerText;
    document.getElementById('editdob').value = new Date(row.cells[5].innerText);
    document.getElementById('editMedicalHistory').value = row.cells[6].innerText;
    document.getElementById('editAddress').value = row.cells[7].innerText;
    document.getElementById('editStatus').value = row.cells[8].innerText.trim(); // Populate with the status text

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
     var patientid = document.getElementById('editID').value;
     var patientname= document.getElementById('editName').value;
     var phonenumber= document.getElementById('editPhoneNumber').value;
     var gender= document.getElementById('editGender').value;
     var date = new Date(document.getElementById('editdob').value).toLocaleDateString('en-US', { day: '2-digit',  month: 'short', year: 'numeric',});
     var medicalhistory= document.getElementById('editMedicalHistory').value;
     var address= document.getElementById('editAddress').value;
     var status = document.getElementById('editStatus').value; // Update status text in table
    

     $.ajax({
        type: "POST",
        url: "/api/update_patient/",
        data: {"id": patientid, "name": patientname, "number" : phonenumber , "gender" : gender ,"dateofbirth" : date, "medicalhistory" : medicalhistory, "address" : address, "status" : status },
        success: function(e)
        {
            window.location.replace("/Doctor/doctor/patientdash");
        }

    });
    if (!currentRow) return; // Prevent saving if no row is selected

    // Close the popup
    closeEditPopup();
}

function closeEditPopup() {
    document.getElementById('editPopup').style.display = 'none';
}

function deleteRow(id) {
    console.log("id: ",id);
    $.ajax({
        type: "POST",
        url: "/api/delete_patient/",
        data: {"id": id},
        success: function(d)
        {
            window.location.replace("/Doctor/doctor/patientdash");
        }

    });

    // Remove the row from the table
   // const row = button.parentNode.parentNode;
    //row.parentNode.removeChild(row);
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
                valA = new Date(a.cells[4].innerText);
                valB = new Date(b.cells[4].innerText);
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

