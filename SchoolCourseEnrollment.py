class Student:
    def __init__(self, name, student_code):
        self.student_name = name
        self.__student_code = student_code

    def display_info(self):
        print(f"Name: {self.student_name}, Student Code: {self.__student_code}")

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.__course_code = course_code
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Only Student instances can be added.")

    def display_students(self):
        print(f"Course: {self.course_name} (Code: {self.__course_code})")
        for student in self.students:
            student.display_info()

student1 = Student("Zeus", "S001")
course1 = Course("Mathematics", "C001")
course1.add_student(student1)
course1.display_students()
student2 = Student("Hera", "S002")
course2 = Course("Physics", "C002")
course2.add_student(student2)   
course2.display_students()
