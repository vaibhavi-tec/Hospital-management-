let editingRow = null;

// Function to add a test to the table
function addTest() {
    const testNameInput = document.getElementById('test-name');
    const testResultInput = document.getElementById('test-result');
    const testCommentsInput = document.getElementById('test-comments');
    const testName = testNameInput.value.trim();
    const testResult = testResultInput.value.trim();
    const testComments = testCommentsInput.value.trim();

    if (testName && testResult) {
        const tableBody = document.querySelector('#tests-table tbody');

        if (editingRow) {
            const rowCells = editingRow.children;
            rowCells[0].textContent = testName;
            rowCells[1].textContent = testResult;
            rowCells[2].textContent = testComments;
            editingRow = null;
        } else {
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
                <td>${testName}</td>
                <td>${testResult}</td>
                <td>${testComments}</td>
                <td>
                    <button class="edit-btn" onclick="editRow(this)">Edit</button>
                    <button class="delete-btn" onclick="deleteRow(this)">Delete</button>
                </td>
            `;
            tableBody.appendChild(newRow);
        }

        testNameInput.value = '';
        testResultInput.value = '';
        testCommentsInput.value = '';
    } else {
        alert("Please enter a valid test name and result.");
    }
}

// Function to edit an existing row
function editRow(button) {
    if (editingRow) return;

    editingRow = button.closest('tr');
    const cells = editingRow.children;
    document.getElementById('test-name').value = cells[0].textContent;
    document.getElementById('test-result').value = cells[1].textContent;
    document.getElementById('test-comments').value = cells[2].textContent;
}

// Function to delete a row
function deleteRow(button) {
    const row = button.closest('tr');
    row.remove();
}

// Function to generate the lab report
function generateReport() {
    const reportNumber = document.getElementById('report-number').value;
    const reportDate = document.getElementById('report-date').value;
    const patientName = document.getElementById('patient-name').value;
    const doctorName = document.getElementById('doctor-name').value;

    const rows = document.querySelectorAll('#tests-table tbody tr');
    let testsHtml = '';
    let testNames = [];
    let testResults = [];

    rows.forEach(row => {
        const testName = row.children[0].textContent;
        const testResult = row.children[1].textContent;
        const testComments = row.children[2].textContent;
        testsHtml += `<tr><td>${testName}</td><td>${testResult}</td><td>${testComments}</td></tr>`;
        testNames.push(testName);
        testResults.push(parseFloat(testResult));
    });

    const reportContent = `
        <h2>Lab Report</h2>
        <p><strong>Report Number:</strong> ${reportNumber}</p>
        <p><strong>Report Date:</strong> ${reportDate}</p>
        <p><strong>Patient Name:</strong> ${patientName}</p>
        <p><strong>Doctor Name:</strong> ${doctorName}</p>
        <h3>Test Results</h3>
        <table border="1" cellspacing="0" cellpadding="5">
            <thead>
                <tr>
                    <th>Test Name</th>
                    <th>Result</th>
                    <th>Comments</th>
                </tr>
            </thead>
            <tbody>
                ${testsHtml}
            </tbody>
        </table>
    `;

    const reportDiv = document.getElementById('report');
    reportDiv.innerHTML = reportContent;
    reportDiv.style.display = 'block';

    // Generate chart for analysis
    generateChart(testNames, testResults);
}

// Function to generate the analysis chart using Chart.js
function generateChart(testNames, testResults) {
    const ctx = document.getElementById('analysis-chart').getContext('2d');
    document.getElementById('analysis-chart').style.display = 'block';

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: testNames,
            datasets: [{
                label: 'Test Results',
                data: testResults,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Function to download the report as a CSV file with "Sudeeksha Hospital" as the header
function downloadCSV() {
    const rows = document.querySelectorAll('#tests-table tbody tr');
    let csvContent = "data:text/csv;charset=utf-8,Sudeeksha Hospital\n";
    csvContent += "Test Name,Result,Comments\n";

    rows.forEach(row => {
        const testName = row.children[0].textContent;
        const testResult = row.children[1].textContent;
        const testComments = row.children[2].textContent;
        csvContent += `${testName},${testResult},${testComments}\n`;
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "lab_report.csv");
    document.body.appendChild(link);
    link.click();
}

// Function to download the report as a PDF file with "Sudeeksha Hospital" as the header
function generatePDF() {
    const { jsPDF } = window.jspdf;  // This fetches the jsPDF constructor

    // Initialize a new PDF document
    const doc = new jsPDF();

    // Set the font and add content
    doc.setFontSize(24);
    doc.text("Sudeeksha Hospital", 10, 10);

    doc.setFontSize(12);
    const reportNumber = document.getElementById('report-number').value;
    const reportDate = document.getElementById('report-date').value;
    const patientName = document.getElementById('patient-name').value;
    const doctorName = document.getElementById('doctor-name').value;

    doc.text(`Report Number: ${reportNumber}`, 10, 30);
    doc.text(`Report Date: ${reportDate}`, 10, 40);
    doc.text(`Patient Name: ${patientName}`, 10, 50);
    doc.text(`Doctor Name: ${doctorName}`, 10, 60);

    let y = 80;
    const rows = document.querySelectorAll('#tests-table tbody tr');

    doc.text("Test Name", 10, y);
    doc.text("Result", 70, y);
    doc.text("Comments", 120, y);

    rows.forEach(row => {
        y += 10;
        const testName = row.children[0].textContent;
        const testResult = row.children[1].textContent;
        const testComments = row.children[2].textContent;
        doc.text(testName, 10, y);
        doc.text(testResult, 70, y);
        doc.text(testComments, 120, y);
    });

    // Save the PDF
    doc.save("lab_report.pdf");
}

