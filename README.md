# Hospital Management System
This project is a Django-based Hospital Management System where the admin can manage hospital records, appointments, and staff. It includes a complete hospital database for easy management.

## Project Structure
The project consists of the following files and directories:

- **Adminsite**: Contains admin-related functionalities.
- **Doctor**: Handles doctor-related functionalities.
- **Management**: Manages hospital operations.
- **Patient**: Contains patient-related models and views.
- **Staff**: Handles staff-related functionalities.
- **static**: Contains static files (CSS, JS, images).
- **templates**: Contains HTML templates for rendering views.
- **manage.py**: A command-line utility for Django projects.
- **README.md**: Project documentation.

## Requirements
This project requires Django to be installed, along with the necessary dependencies as specified in `requirements.txt`.

## Setting Up a Virtual Environment
To set up a virtual environment and install Django, follow these steps:

1. Open your command prompt or terminal.
2. Create a virtual environment using the following command:
   ```sh
   python -m venv hospital_env
   ```
3. Navigate into the virtual environment directory:
   ```sh
   cd hospital_env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```sh
     cd Scripts
     activate
     ```
   - On macOS/Linux:
     ```sh
     source bin/activate
     ```
5. Inside the activated virtual environment, install Django:
   ```sh
   pip install django
   ```

## Usage
After setting up the virtual environment and installing Django, navigate to your project directory.

Run the following command to start the Django server:
```sh
python manage.py runserver
```

Access the application in your web browser at `http://127.0.0.1:8000/`.

## Features
### Admin can add, update, and delete:
- Doctors
- Patients
- Staff members
- Appointments
- Hospital records

### Doctors can:
- View and manage their appointments
- Update patient records

### Patients can:
- Book appointments
- View their medical history

### Staff can:
- Manage hospital facilities
- Handle administrative tasks

This application provides a complete hospital database for management and user interaction.

## Acknowledgements
Thank you for using the Hospital Management System! We hope it enhances your experience in managing hospital data efficiently.


