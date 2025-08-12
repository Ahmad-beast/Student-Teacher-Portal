# Student, Teacher & Admin Portal 🎓

A **console-based portal system** developed using **Python Object-Oriented Programming (OOP)**.  
This project simulates a **university or school management system** with three distinct user roles:  
**Student 🧑‍🎓**, **Teacher 🧑‍🏫**, and **Administrator 💼**.

The system uses **file handling** to persist data and demonstrates core OOP principles like **inheritance**, **encapsulation**, and **polymorphism**.

---

## ✨ Features

### 👨‍🎓 Student Features
- **Enroll & Unenroll:** Students can enroll in available course sections. Enrollment is restricted if a section's capacity is full.
- **Academic Records:** View semester-wise CGPA and academic history.
- **Performance Visualization:** Plot CGPA trends over semesters using `matplotlib`.
- **View Teacher Profiles:** Access and view the profiles of teachers.
- **Password Management:** Students can change their own passwords for security.

### 👩‍🏫 Teacher Features
- **Profile Management:** Add, update, or delete personal and professional information.
- **Salary Slips:** View detailed salary slips.
- **Password Management:** Change password securely.

### 💼 Admin Features
- **Full Data Access:** Complete oversight of all student and teacher data.
- **User Creation:** Automatically generate unique IDs and default passwords for new students and teachers.
- **System Monitoring:** View logs of updates made by teachers and manage enrollments.
- **System Statistics:** Snapshot of key metrics like total user counts and course enrollments.

---

## 🛠️ Technologies & Concepts

### **Core Concepts**
- **Object-Oriented Programming (OOP)**:
  - **Inheritance:** Base `User` class extended by `Student`, `Teacher`, and `Admin` subclasses.
  - **Encapsulation:** Passwords and sensitive data kept private within classes.
  - **Polymorphism:** Methods like `view_profile()` overridden in subclasses for role-specific behavior.
- **File Handling:** Data stored in `.json` files for persistence.
- **Data Visualization:** Academic performance charts with `matplotlib`.
- **Data Structures:** Lists & dictionaries for efficient in-memory operations.

---

## 🚀 Getting Started

### **Prerequisites**
- Python 3 installed → [Download here](https://www.python.org/downloads/)
- `pip` package manager installed

### **Installation & Setup**

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```
---
### 2️⃣ Install Dependencies
```bash
pip install matplotlib
```
---
### 3️⃣ Run the Setup Script
```bash
python setup_data.py
```

### This will create sample data files:
```bash
students.json
teachers.json
admins.json
courses.json
```
---
### 4️⃣ Launch the Application 🎉
```bash
python main.py
```
---

## 💻 How to Use

- Start the application — you’ll be prompted for username and password.
- Use the pre-generated credentials from .json files.

### Login Credentials

#### 🧑‍🎓 Student Logins
   ```bash
   Username: student1
   Password: pass1
```
#### 🧑‍🎓🧑‍🏫 Teacher Logins
   ```bash
   Username: teacher1
   Password: tpass1
```
#### 💼 Admin Login
   ```bash
   Username: admin
   Password: admin
```

##### After login, a role-specific menu will appear with relevant options.
---

### 📌 Notes
- Data persistence is handled via `.json` files.
- Charts require matplotlib to be installed.
- Default credentials are for demo purposes — change passwords after first login.

---



I’ve kept it **GitHub-friendly** with:
- Clear sections
- Emojis for quick scanning
- Proper code blocks for commands & credentials
- Professional formatting  

If you want, I can also add **badges** (Python version, License, Stars, Forks) at the top to make it look like a polished open-source project. That would give it a very professional look.














