# DEPI_Round_4_Machine_Learning
# Employee Management System (EMS)

A professional, Object-Oriented Python application designed for managing employee records. This system utilizes a Graphical User Interface (GUI) and maintains persistent data storage using the Python `csv` module.

## 🚀 Project Overview

The Employee Management System is built to handle core HR tasks efficiently. It follows the **Separation of Concerns** principle, ensuring that the data processing logic is completely decoupled from the user interface.

### 🛠️ System Architecture

The project is divided into two primary modules:

1.  **`main.py` (Business Logic Layer):**
    * Manages the `EmployeeManager` class.
    * Handles all dictionary-based in-memory storage.
    * Performs CRUD (Create, Read, Update, Delete) operations and file I/O.
2.  **`gui_app.py` (Presentation Layer):**
    * Manages the `EmployeeGUI` class.
    * Handles window construction, event loops, and interactive table rendering.



---

## ⚙️ Logic & Functionality

* **Dictionary-Based Storage:** To ensure high performance, the system loads all CSV data into a Python dictionary upon startup. This allows for **O(1) time complexity** during search and update operations.
* **Persistent Saving:** The system uses an "Atomic Save" methodology—every successful change in the UI triggers an immediate update to the `employees.csv` file.
* **Partial Updates:** The update logic is designed to be non-destructive. If a user leaves an input field blank during an update, the system preserves the existing data for that field rather than overwriting it with an empty string.

---

## 🛡️ Technical Constraints & Validation

To ensure data integrity, the system enforces the following strict rules:

### 1. Data Integrity
* **Primary Key Uniqueness:** The `ID` must be unique. The system rejects "Add" operations if the ID already exists.
* **Type Safety:** * `ID` must be a numeric integer.
    * `Salary` must be a positive numeric value (float).
* **Length Limits:** * **Name:** Max 50 characters.
    * **Position:** Max 30 characters.
    * **Email:** Max 50 characters.

### 2. Format Validation
* **Email Regex:** Emails are validated against a standard pattern (`user@domain.com`) using Python's `re` module.



---

## 🖥️ Graphical User Interface (GUI)

The GUI is designed for speed and ease of use:

* **Interactive Treeview:** Displays all employees in a clean table format.
* **Click-to-Fill:** Selecting a row in the table automatically populates the input fields, allowing for rapid editing or deletion.
* **Color-Coded Actions:** * 🟢 **Add:** Light Green
    * 🟡 **Update:** Light Yellow
    * 🔴 **Delete:** Light Red
* **Status Bar:** Provides a real-time count of total records currently stored in the system.
* **Clear Utility:** A dedicated "Clear Fields" button to reset the form instantly.

---

## 📋 Requirements & Setup

* **Python Version:** 3.8+
* **No External Dependencies:** Uses standard libraries exclusively (`tkinter`, `csv`, `os`, `re`).

### Execution:
Ensure `main.py` and `gui_app.py` are in the same folder, then run:
```bash
python gui_app.py