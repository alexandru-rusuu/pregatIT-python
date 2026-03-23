from live_coding.model.Student import Student
from live_coding.service.DatabaseStorageService import init_db, save_students_to_db, load_students_from_db, save_student


def main():
    print("Initializing database...")
    init_db()

    # Create some sample students
    students = [
        Student("Alice Smith", (15, 5, 2000), "Computer Science", [85, 90, 78]),
        Student("Bob Jones", (22, 11, 1999), "Mathematics", [70, 65, 80]),
        Student("Charlie Brown", (10, 1, 2001), "Physics", [95, 88, 92])
    ]

    print(f"Saving {len(students)} students to the database...")
    save_students_to_db(students)

    print("Loading students from the database...")
    loaded_students = load_students_from_db()

    print("\nLoaded Students:")
    for student in loaded_students:
        print(student)

    studentA = Student("Alice Smith", (15, 5, 2000), "Computer Science", [85, 90, 78])
    studentA = save_student(studentA)
    print(f"Added student with ID: {studentA}")

    # delete_student_by_id(studentA.id)
    # print("Student deleted")



if __name__ == "__main__":
    main()
