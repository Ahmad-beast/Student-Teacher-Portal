import json

def setup_initial_data():
    # --- Student Data ---
    students = {
        f"student{i}": {
            "password": f"pass{i}",
            "student_id": f"S00{i}",
            "enrolled_courses": [],
            "academic_records": {
                "Semester 1": 3.5,
                "Semester 2": 3.7
            }
        } for i in range(1, 13) # 12 students
    }
    
    # --- Teacher Data ---
    teachers = {
        f"teacher{i}": {
            "password": f"tpass{i}",
            "teacher_id": f"T0{i}",
            "personal_info": {
                "name": f"Teacher Name {i}",
                "qualification": "PhD in Computer Science",
                "contact": f"123-456-78{i:02d}"
            },
            "salary": 60000 + (i * 1000)
        } for i in range(1, 11) # 10 teachers
    }

    # --- Admin Data ---
    admins = {
        "admin": {
            "password": "admin"
        }
    }

    # --- Course Data ---
    courses = {
        "CS101": {
            "name": "Introduction to Programming",
            "sections": [
                {"section_id": "CS101-A", "teacher": "T01", "capacity": 30, "students": []},
                {"section_id": "CS101-B", "teacher": "T02", "capacity": 3, "students": ["S001", "S002", "S003"]} # Full Section
            ]
        },
        "MA202": {
            "name": "Calculus II",
            "sections": [
                {"section_id": "MA202-A", "teacher": "T03", "capacity": 25, "students": []}
            ]
        }
    }

    # --- File Handling: Save to JSON files ---
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)
    
    with open('teachers.json', 'w') as f:
        json.dump(teachers, f, indent=4)
        
    with open('admins.json', 'w') as f:
        json.dump(admins, f, indent=4)

    with open('courses.json', 'w') as f:
        json.dump(courses, f, indent=4)
    
    print("Initial data has been set up successfully.")
    print("Files created: students.json, teachers.json, admins.json, courses.json")

if __name__ == "__main__":
    setup_initial_data()