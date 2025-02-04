let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editName').value = row.cells[1].innerText.trim();
    document.getElementById('editEmail').value = row.cells[2].innerText;
    document.getElementById('editDate').value = new Date(row.cells[3].innerText).toISOString().substr(0, 10);
    document.getElementById('editFrom').value = row.cells[4].innerText;
    document.getElementById('editTo').value = row.cells[5].innerText;
    document.getElementById('editMobile').value = row.cells[6].innerText;
    document.getElementById('editDoctor').value = row.cells[7].innerText;
    document.getElementById('editCondition').value = row.cells[8].innerText;

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    currentRow.cells[1].innerText = document.getElementById('editName').value;
    currentRow.cells[2].innerText = document.getElementById('editEmail').value;
    currentRow.cells[3].innerText = new Date(document.getElementById('editDate').value).toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric' });
    currentRow.cells[4].innerText = document.getElementById('editFrom').value;
    currentRow.cells[5].innerText = document.getElementById('editTo').value;
    currentRow.cells[6].innerText = document.getElementById('editMobile').value;
    currentRow.cells[7].innerText = document.getElementById('editDoctor').value;
    currentRow.cells[8].innerText = document.getElementById('editCondition').value;

    // Close the popup
    closeEditPopup();
}

function closeEditPopup() {
    document.getElementById('editPopup').style.display = 'none';
}

function deleteRow(button) {
    // Remove the row from the table
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
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
document.getElementById('newAppointmentBtn').addEventListener('click', function() {
    alert("This feature to add a new appointment is under development.");
});

