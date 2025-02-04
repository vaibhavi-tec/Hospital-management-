let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editID').value = row.cells[1].innerText.trim();
    document.getElementById('editDate').value = row.cells[2].innerText;
    document.getElementById('editWID').value = row.cells[3].innerText;
    
    document.getElementById('editpname').value = row.cells[4].innerText;
    document.getElementById('editdname').value = row.cells[5].innerText;
    document.getElementById('editstat').value = row.cells[6].innerText;
    document.getElementById('editpre').value = row.cells[7].innerText;

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    var editid = document.getElementById('editID').value;
    var wid = document.getElementById('editWID').value;
    var date  = new Date(document.getElementById('editDate').value).toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric' });
    var pname = document.getElementById('editpname').value;
    var dname = document.getElementById('editdname').value;
    var stat = document.getElementById('editstat').value;
    var pre = document.getElementById('editpre').value;

    $.ajax({
        type: "POST",
        url: "/api/update_bed/",
        data: {"id": editid, "wid": wid ,"pname" : pname ,"dname" : dname , "stat": stat, "pre":pre},
        success: function(e)
        {
            window.location.replace("/Staff/Staff/beddash");
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
    console.log("id: ",id);
    $.ajax({
        type: "POST",
        url: "/api/delete_bed/",
        data: {"id": id},
        success: function(d)
        {
            window.location.replace("/Staff/Staff/beddash");
        }

    });
}

document.getElementById('filterBtn').addEventListener('click', function() {
    const filterOptions = document.getElementById('filterOptions');
    filterOptions.style.display = filterOptions.style.display === 'none' ? 'block' : 'none';
});

function sortTable(column, order) {
    const table = document.getElementById('Bedtable').getElementsByTagName('tbody')[0];
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



