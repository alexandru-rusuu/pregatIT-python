from live_coding.model.Student import Student
from live_coding.service.FileStorageService import load_students, save_students
from live_coding.service.PythonClassService import is_student_passing, get_not_passing_grades

if __name__ == '__main__':


    studentA = Student("Andrei", (2,12,1993), "IT", [50, 34, 50])

    if is_student_passing(studentA):
        print("Student is passing")
    else:
        not_passing_grades = get_not_passing_grades(studentA)
        print(f"Student is not passing because he has these grades: {not_passing_grades}")




