import json
import os
import matplotlib.pyplot as plt

# --- BASE USER CLASS ---
class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def login(self, username, password):
        return self._username == username and self._password == password

    def change_password(self, new_password):
        self._password = new_password
        self.save_credentials() # Assumes a method to save changes to a file
        print("Password changed successfully.")

    def view_profile(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def get_username(self):
        return self._username

    def save_credentials(self):
        # This method would be more fleshed out in a real application
        # For this example, we'll simulate saving to a dictionary that represents our user database
        print(f"Saving credentials for {self._username}")


# --- STUDENT CLASS ---
class Student(User):
    def __init__(self, username, password, student_id, academic_records=None, enrolled_courses=None):
        super().__init__(username, password)
        self.student_id = student_id
        self.enrolled_courses = enrolled_courses if enrolled_courses is not None else []
        self.academic_records = academic_records if academic_records is not None else {}

    def enroll_in_course(self, course_section):
        if len(course_section['students']) < course_section['capacity']:
            self.enrolled_courses.append(course_section['section_id'])
            course_section['students'].append(self.student_id)
            print(f"Successfully enrolled in {course_section['section_id']}.")
            self.save_to_file()
        else:
            print("Enrollment failed: The section is full.")

    def unenroll_from_course(self, course_id):
        if course_id in self.enrolled_courses:
            self.enrolled_courses.remove(course_id)
            print(f"Successfully unenrolled from {course_id}.")
            self.save_to_file()
        else:
            print("You are not enrolled in this course.")

    def view_academic_record(self):
        print("--- Academic Record ---")
        for semester, gpa in self.academic_records.items():
            print(f"  {semester}: CGPA = {gpa}")

    def plot_cgpa_trend(self):
        semesters = list(self.academic_records.keys())
        gpas = list(self.academic_records.values())
        if not semesters or not gpas:
            print("No academic data available to plot.")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(semesters, gpas, marker='o', linestyle='-')
        plt.title('CGPA Trend Over Semesters')
        plt.xlabel('Semester')
        plt.ylabel('CGPA')
        plt.grid(True)
        plt.show()

    def view_teacher_profile(self, teacher_username, teachers_data):
        teacher_info = teachers_data.get(teacher_username)
        if teacher_info:
            print(f"\n--- Teacher Profile: {teacher_username} ---")
            for key, value in teacher_info.get('personal_info', {}).items():
                print(f"  {key.capitalize()}: {value}")
        else:
            print("Teacher not found.")

    def save_to_file(self):
        # In a real app, this would write to a student-specific file
        print(f"Saving data for student {self.student_id}...")

    def view_profile(self):
        print(f"\n--- Student Profile ---")
        print(f"  ID: {self.student_id}")
        print(f"  Username: {self._username}")
        print(f"  Enrolled Courses: {', '.join(self.enrolled_courses)}")


# --- TEACHER CLASS ---
class Teacher(User):
    def __init__(self, username, password, teacher_id, personal_info=None, salary=0):
        super().__init__(username, password)
        self.teacher_id = teacher_id
        self.personal_info = personal_info if personal_info is not None else {}
        self.salary = salary

    def view_salary_slip(self):
        print(f"\n--- Salary Slip for {self.teacher_id} ---")
        print(f"  Salary: ${self.salary}")

    def add_personal_info(self, info):
        self.personal_info.update(info)
        print("Personal information added successfully.")
        self.save_to_file()

    def update_personal_info(self, info):
        self.personal_info.update(info)
        print("Personal information updated successfully.")
        self.save_to_file()

    def delete_personal_info(self, key):
        if key in self.personal_info:
            del self.personal_info[key]
            print(f"'{key}' has been deleted from your personal information.")
            self.save_to_file()
        else:
            print(f"'{key}' not found in your personal information.")

    def save_to_file(self):
         # In a real app, this would write to a teacher-specific file
        print(f"Saving data for teacher {self.teacher_id}...")

    def view_profile(self):
        print(f"\n--- Teacher Profile ---")
        print(f"  ID: {self.teacher_id}")
        print(f"  Username: {self._username}")
        for key, value in self.personal_info.items():
            print(f"  {key.capitalize()}: {value}")


# --- ADMIN CLASS ---
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def create_user_id(self, user_type, existing_ids):
        import random
        import string
        prefix = "S" if user_type.lower() == 'student' else 'T'
        while True:
            new_id = prefix + ''.join(random.choices(string.digits, k=5))
            if new_id not in existing_ids:
                return new_id, 'password123' # Auto-generated password

    def view_all_student_data(self, students_data):
        print("\n--- All Student Data ---")
        for username, data in students_data.items():
            print(f"  Student ID: {data['student_id']}, Username: {username}")

    def view_all_teacher_data(self, teachers_data):
        print("\n--- All Teacher Data ---")
        for username, data in teachers_data.items():
            print(f"  Teacher ID: {data['teacher_id']}, Username: {username}")

    def view_system_statistics(self, students_data, teachers_data, courses_data):
        print("\n--- System Statistics ---")
        print(f"  Total Students: {len(students_data)}")
        print(f"  Total Teachers: {len(teachers_data)}")
        total_enrollments = sum(len(section['students']) for course in courses_data.values() for section in course['sections'])
        print(f"  Total Course Enrollments: {total_enrollments}")
        
    def view_profile(self):
        print(f"\n--- Admin Profile ---")
        print(f"  Username: {self._username}")
        print("  Access Level: Full System Control")


# --- DATA MANAGEMENT ---
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# --- MENUS ---
def student_menu(student, all_data):
    while True:
        print("\n--- Student Menu ---")
        print("1. Enroll in a Course")
        print("2. Unenroll from a Course")
        print("3. View Academic Record")
        print("4. Plot CGPA Trend")
        print("5. View Teacher Profile")
        print("6. Change Password")
        print("7. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Simplified enrollment process
            print("Available Course Sections:")
            for course_id, course_info in all_data['courses'].items():
                 for section in course_info['sections']:
                    print(f"  - {section['section_id']} ({course_info['name']})")
            section_id = input("Enter section ID to enroll: ")
            
            section_found = None
            for course_info in all_data['courses'].values():
                for section in course_info['sections']:
                    if section['section_id'] == section_id:
                        section_found = section
                        break
                if section_found:
                    break
            
            if section_found:
                 student.enroll_in_course(section_found)
                 save_data('courses.json', all_data['courses'])
            else:
                 print("Section not found.")

        elif choice == '2':
            course_id = input("Enter course ID to unenroll: ")
            student.unenroll_from_course(course_id)
        elif choice == '3':
            student.view_academic_record()
        elif choice == '4':
            student.plot_cgpa_trend()
        elif choice == '5':
            teacher_username = input("Enter teacher's username to view profile: ")
            student.view_teacher_profile(teacher_username, all_data['teachers'])
        elif choice == '6':
            new_pass = input("Enter new password: ")
            student.change_password(new_pass)
            # In a real app, update the main data structure and save
        elif choice == '7':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")

def teacher_menu(teacher):
    while True:
        print("\n--- Teacher Menu ---")
        print("1. View Salary Slip")
        print("2. Update Personal Information")
        print("3. Change Password")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            teacher.view_salary_slip()
        elif choice == '2':
            key = input("What information to update/add (e.g., qualification, contact): ")
            value = input(f"Enter new {key}: ")
            teacher.update_personal_info({key: value})
        elif choice == '3':
            new_pass = input("Enter new password: ")
            teacher.change_password(new_pass)
        elif choice == '4':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")


def admin_menu(admin, all_data):
    while True:
        print("\n--- Admin Menu ---")
        print("1. View All Student Data")
        print("2. View All Teacher Data")
        print("3. View System Statistics")
        print("4. Create New User")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin.view_all_student_data(all_data['students'])
        elif choice == '2':
            admin.view_all_teacher_data(all_data['teachers'])
        elif choice == '3':
            admin.view_system_statistics(all_data['students'], all_data['teachers'], all_data['courses'])
        elif choice == '4':
            user_type = input("Create 'student' or 'teacher': ")
            if user_type.lower() in ['student', 'teacher']:
                existing_ids = [d['student_id'] for d in all_data['students'].values()] + [d['teacher_id'] for d in all_data['teachers'].values()]
                new_id, new_pass = admin.create_user_id(user_type, existing_ids)
                username = input("Enter a username for the new user: ")
                
                if user_type.lower() == 'student':
                    all_data['students'][username] = {
                        "password": new_pass, "student_id": new_id, 
                        "enrolled_courses": [], "academic_records": {}
                    }
                    save_data('students.json', all_data['students'])
                else: # teacher
                    all_data['teachers'][username] = {
                        "password": new_pass, "teacher_id": new_id, 
                        "personal_info": {}, "salary": 50000 # default salary
                    }
                    save_data('teachers.json', all_data['teachers'])
                print(f"New {user_type} created. ID: {new_id}, Username: {username}, Password: {new_pass}")
            else:
                print("Invalid user type.")

        elif choice == '5':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")

# --- MAIN APPLICATION LOGIC ---
def main():
    # Load all data from files
    all_data = {
        'students': load_data('students.json'),
        'teachers': load_data('teachers.json'),
        'admins': load_data('admins.json'),
        'courses': load_data('courses.json')
    }
    
    # Check if initial data setup is needed
    if not all_data['students']:
        print("No student data found. Please run the setup script first.")
        # You might want to call a setup function here if running for the first time
        # For now, we will assume setup_data.py has been run.
        return

    print("--- Welcome to the University Portal ---")
    
    while True:
        username = input("Username: ")
        password = input("Password: ")

        user_role = None
        user_data = None

        if username in all_data['students'] and all_data['students'][username]['password'] == password:
            user_role = 'student'
            user_data = all_data['students'][username]
            current_user = Student(username, password, user_data['student_id'], user_data['academic_records'], user_data['enrolled_courses'])
            print(f"\nWelcome {username}! (Student)")
            student_menu(current_user, all_data)
            
        elif username in all_data['teachers'] and all_data['teachers'][username]['password'] == password:
            user_role = 'teacher'
            user_data = all_data['teachers'][username]
            current_user = Teacher(username, password, user_data['teacher_id'], user_data['personal_info'], user_data.get('salary'))
            print(f"\nWelcome {username}! (Teacher)")
            teacher_menu(current_user)

        elif username in all_data['admins'] and all_data['admins'][username]['password'] == password:
            user_role = 'admin'
            current_user = Admin(username, password)
            print(f"\nWelcome {username}! (Admin)")
            admin_menu(current_user, all_data)
        
        else:
            print("Invalid username or password.")
        
        # Ask if user wants to login again or exit
        if input("Log in with another account? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()