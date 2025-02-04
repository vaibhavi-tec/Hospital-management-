let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editID').value = row.cells[1].innerText.trim();
    document.getElementById('editname').value = row.cells[2].innerText;
    document.getElementById('editapp').value = row.cells[3].innerText;
    document.getElementById('editdate').value = new Date(row.cells[4].innerText).toISOString().substr(0, 10);
    document.getElementById('editStatus').value = row.cells[5].innerText;
    document.getElementById('editAm').value = row.cells[6].innerText;
   
    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    var paymentid = document.getElementById('editID').value;
    var name = document.getElementById('editname').value;
    var appointmentid = document.getElementById('editapp').value;
    var date = new Date(document.getElementById('editdate').value).toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric' });
    var status= document.getElementById('editStatus').value;
    var amount = document.getElementById('editAm').value;
    $.ajax({
        type: "POST",
        url: "/api/update_payment/",
        data: {"id": paymentid, "name": name,"app" :appointmentid  ,"date" : date ,"status" : status, "am" : amount},
        success: function(e)
        {
            window.location.replace("/Staff/Staff/paydash");
        }

    });
    if (!currentRow) return; // Prevent saving if no row is selected



    closeEditPopup();
}

function closeEditPopup() {
    document.getElementById('editPopup').style.display = 'none';
}

function deleteRow(button) {
    console.log("id: ",id);
    $.ajax({
        type: "POST",
        url: "/api/delete_payment/",
        data: {"id": id},
        success: function(d)
        {
            window.location.replace("/Staff/Staff/paydash");
        }

    });

    // Remove the row from the table
   // const row = button.parentNode.parentNode;
  //  row.parentNode.removeChild(row);
}

document.getElementById('filterBtn').addEventListener('click', function() {
    const filterOptions = document.getElementById('filterOptions');
    filterOptions.style.display = filterOptions.style.display === 'none' ? 'block' : 'none';
});

function sortTable(column, order) {
    const table = document.getElementById('PaymentTable').getElementsByTagName('tbody')[0];
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
;