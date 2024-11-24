# Student Registration and Viewer App

This project is a simple web-based application for registering student details and viewing the registered students. It consists of an HTML front-end for user interaction and a Python Flask back-end (`app.py`) to handle data storage and retrieval.

---

## Features

1. **Student Registration**:
   - Users can input student details including name, registration number, mobile number, email, and location.
   - Form validations ensure proper input formats before submission.
   - Displays a success message upon successful registration.

2. **View Registered Students**:
   - Allows users to fetch and view the list of all registered students.
   - Displays the data in a table format.

---

## Prerequisites

- Python (3.7 or higher)
- Flask (`pip install flask`)
- A browser to load the HTML file

---


---

## How to Run

1. **Set Up the Environment**:
   - Ensure Python is installed on your machine.
   - Install Flask using pip:
     ```bash
     pip install flask
     ```

2. **Run the Flask Server**:
   - Open a terminal in the directory containing `app.py`.
   - Start the server:
     ```bash
     python app.py
     ```
   - By default, the Flask server will run at `http://127.0.0.1:5000`.

3. **Open the Application**:
   - Open a web browser and go to:
     ```
     http://127.0.0.1:5000
     ```

4. **Use the App**:
   - Fill in the form fields to register a student.
   - Click "Register" to save the details.
   - Click "Show Registered Students" to view the list of all registered students.

---

## License

This project is open-source and available for personal or educational use.
