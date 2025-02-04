let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editID').value = row.cells[1].innerText.trim();
    document.getElementById('editPID').value = row.cells[2].innerText;
  
    document.getElementById('editname').value = row.cells[3].innerText;
    document.getElementById('editFlr').value = row.cells[4].innerText;
    document.getElementById('editquan').value = row.cells[5].innerText;
    document.getElementById('editava').value = row.cells[6].innerText;

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    var editid = document.getElementById('editID').value;
    var pid = document.getElementById('editPID').value;
    var name = document.getElementById('editname').value;
    var floor = document.getElementById('editFlr').value;
    var quan = document.getElementById('editquan').value;
    var ava = document.getElementById('editava').value;

    $.ajax({
        type: "POST",
        url: "/api/update_ward/",
        data: {"id": editid, "Pid": pid ,"name" : name ,"floor" : floor ,"quan" : quan , "ava": ava},
        success: function(e)
        {
            window.location.replace("/Staff/Staff/warddashh");
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
    // Remove the row from the table
    console.log("id: ",id);
    $.ajax({
        type: "POST",
        url: "/api/delete_ward/",
        data: {"id": id},
        success: function(d)
        {
            window.location.replace("/Staff/Staff/warddash");
        }

    });
}

document.getElementById('filterBtn').addEventListener('click', function() {
    const filterOptions = document.getElementById('filterOptions');
    filterOptions.style.display = filterOptions.style.display === 'none' ? 'block' : 'none';
});

function sortTable(column, order) {
    const table = document.getElementById('Wardtable').getElementsByTagName('tbody')[0];
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


