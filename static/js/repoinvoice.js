// script.js
let editingRow = null;

function addCharge() {
    const descriptionInput = document.getElementById('charge-description');
    const amountInput = document.getElementById('charge-amount');
    const description = descriptionInput.value.trim();
    const amount = parseFloat(amountInput.value.trim());

    if (description && !isNaN(amount) && amount >= 0) {
        const tableBody = document.querySelector('#charges-table tbody');

        if (editingRow) {
            // Update existing row
            const rowCells = editingRow.children;
            rowCells[0].textContent = description;
            rowCells[1].textContent = `$${amount.toFixed(2)}`;
            editingRow = null;
        } else {
            // Add new row
            const newRow = document.createElement('tr');

            newRow.innerHTML = `
                <td>${description}</td>
                <td>$${amount.toFixed(2)}</td>
                <td>
                    <button class="edit-btn" onclick="editRow(this)">Edit</button>
                    <button class="delete-btn" onclick="deleteRow(this)">Delete</button>
                </td>
            `;

            tableBody.appendChild(newRow);
        }

        updateTotal();
        descriptionInput.value = '';
        amountInput.value = '';
    } else {
        alert("Please enter valid description and amount.");
    }
}

function editRow(button) {
    if (editingRow) return; // Prevent editing multiple rows at once

    editingRow = button.closest('tr');
    const cells = editingRow.children;
    document.getElementById('charge-description').value = cells[0].textContent;
    document.getElementById('charge-amount').value = parseFloat(cells[1].textContent.replace('$', '')).toFixed(2);
}

function deleteRow(button) {
    const row = button.closest('tr');
    row.remove();
    updateTotal();
}

function updateTotal() {
    const rows = document.querySelectorAll('#charges-table tbody tr');
    let total = 0;

    rows.forEach(row => {
        const amountCell = row.querySelector('td:nth-child(2)');
        const amount = parseFloat(amountCell.textContent.replace('$', ''));
        total += amount;
    });

    document.getElementById('total-amount').textContent = total.toFixed(2);
}

function generateInvoice() {
    const billNumber = document.getElementById('bill-number').value;
    const billDate = document.getElementById('bill-date').value;
    const patientName = document.getElementById('patient-name').value;
    const doctorName = document.getElementById('doctor-name').value;
    const paymentMethod = document.getElementById('payment-method').value;
    const paymentStatus = document.getElementById('payment-status').value;
    const totalAmount = document.getElementById('total-amount').textContent;

    // Gather charges
    const rows = document.querySelectorAll('#charges-table tbody tr');
    let chargesHtml = '';

    rows.forEach(row => {
        const description = row.children[0].textContent;
        const amount = row.children[1].textContent;
        chargesHtml += `<tr><td>${description}</td><td>${amount}</td></tr>`;
    });

    const invoiceContent = `
        <style>
            .invoice-header {
                text-align: center;
                margin-bottom: 20px;
            }
            .invoice-logo {
                width: 100px;
                height: auto;
                display: block;
                margin: 0 auto;
            }
            .invoice-title {
                font-size: 24px;
                font-weight: bold;
            }
            .invoice-address {
                margin: 10px 0;
            }
            .invoice-line {
                border: 1px solid blue;
                margin: 10px 0;
            }
            .invoice-body {
                font-family: Arial, sans-serif;
                margin: 0 auto;
                width: 80%;
            }
            .invoice-main-heading {
                text-align: center;
                margin-bottom: 20px;
                font-size: 22px;
                font-weight: bold;
            }
            .invoice-details {
                margin-bottom: 20px;
            }
            .invoice-detail-item {
                display: flex;
                margin-bottom: 10px;
            }
            .detail-label {
                font-weight: bold;
            }
            .charges-heading {
                text-align: center;
                margin: 20px 0;
                font-size: 20px;
                font-weight: bold;
            }
            .charges-table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            .charges-table th, .charges-table td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            .invoice-total {
                display: flex;
                text-align: right;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .print-button {
                display: block;
                width: 100%;
                padding: 10px;
                background-color: #007bff;
                color: white;
                border: none;
                cursor: pointer;
                font-size: 16px;
            }
        </style>

        <div class="invoice-header">
            <img src="{% static '/images/logo.png' %}" alt="SG Hospital Logo" class="invoice-logo">
            <div class="invoice-title">SG Hospital</div>
            <p class="invoice-address">123 Hospital Lane, City, Country</p>
            <hr class="invoice-line">
        </div>
        <div class="invoice-body">
            <h2 class="invoice-main-heading">Patient Invoice</h2>
            <div class="invoice-details">
                <div class="invoice-detail-item">
                    <span class="detail-label">Patient Name: </span>
                    <span class="detail-value">${patientName}</span>
                </div>
                <div class="invoice-detail-item">
                    <span class="detail-label">Bill Number: </span>
                    <span class="detail-value">${billNumber}</span>
                </div>
                <div class="invoice-detail-item">
                    <span class="detail-label">Doctor Name: </span>
                    <span class="detail-value">${doctorName}</span>
                </div>
                <div class="invoice-detail-item">
                    <span class="detail-label">Bill Date: </span>
                    <span class="detail-value">${billDate}</span>
                </div>
                <div class="invoice-detail-item">
                    <span class="detail-label">Payment Method: </span>
                    <span class="detail-value">${paymentMethod}</span>
                </div>
                <div class="invoice-detail-item">
                    <span class="detail-label">Payment Status: </span>
                    <span class="detail-value">${paymentStatus}</span>
                </div>
            </div>
            <h3 class="charges-heading">Charges</h3>
            <table class="charges-table">
                <thead>
                    <tr>
                        <th>Description</th>
                        <th>Amount</th>
                    </tr>
                </thead>
                <tbody>
                    ${chargesHtml}
                </tbody>
            </table>
            <div class="invoice-total">
                <span class="total-label">Total Price: </span>
                <span class="total-value">$${totalAmount}</span>
            </div>
            
        </div>
        <button class="print-button" onclick="printInvoice()">Print Invoice</button>
    `;

    const invoiceDiv = document.getElementById('invoice');
    invoiceDiv.innerHTML = invoiceContent;
    invoiceDiv.style.display = 'block';
}


function printInvoice() {
    const printWindow = window.open('', '', 'height=600,width=800');
    printWindow.document.write('<html><head><title>Invoice</title>');
    // Include inline CSS styles here
    printWindow.document.write(`
        <style>
            .invoice-header {
                text-align: center;
                margin-bottom: 20px;
            }
            .invoice-logo {
                width: 100px;
                height: auto;
                display: block;
                margin: 0 auto;
            }
            .invoice-title {
                font-size: 24px;
                font-weight: bold;
            }
            .invoice-address {
                margin: 10px 0;
            }
            .invoice-line {
                border: 1px solid blue;
                margin: 10px 0;
            }
            .invoice-body {
                font-family: Arial, sans-serif;
                margin: 0 auto;
                width: 80%;
            }
            .invoice-main-heading {
                text-align: center;
                margin-bottom: 20px;
                font-size: 22px;
                font-weight: bold;
            }
            .invoice-details {
                margin-bottom: 20px;
            }
            .invoice-detail-item {
                display: flex;
                margin-bottom: 10px;
            }
            .detail-label {
                font-weight: bold;
            }
            .charges-heading {
                text-align: center;
                margin: 20px 0;
                font-size: 20px;
                font-weight: bold;
            }
            .charges-table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            .charges-table th, .charges-table td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            .invoice-total {
                display: flex;
                text-align: right;
                font-weight: bold;
                margin-bottom: 20px;
            }
            
        </style>
    `);
    printWindow.document.write('</head><body>');
    printWindow.document.write(document.getElementById('invoice').innerHTML);
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
}

