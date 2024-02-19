class Person:
    def display_details(self):
        pass


class Student(Person):
    def __init__(self, student_id, name):
        self.__student_id = student_id  # Access modifier to prohibit direct access
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number")
        self.grades[subject] = grade

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def display_details(self):
        return f"ID: {self.__student_id}, Name: {self.name}, Average Grade: {self.average_grade()}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added")
        self.students.append(student)

    def show_student_details(self, student_id):
        for student in self.students:
            if student._Student__student_id == student_id:  # Accessing private attribute
                return student.display_details()
        return "Student not found."

    def show_student_average_grade(self, student_id):
        for student in self.students:
            if student._Student__student_id == student_id:  # Accessing private attribute
                return student.average_grade()
        return "Student not found."


# Example Usage:
if __name__ == "__main__":
    # Creating students
    student1 = Student(1, "Alice")
    student2 = Student(2, "Bob")

    # Adding grades
    student1.add_grade("Math", 90)
    student1.add_grade("Science", 85)
    student2.add_grade("Math", 75)
    student2.add_grade("Science", 80)

    # Creating student management system
    sms = StudentManagementSystem()

    # Adding students to the system
    sms.add_student(student1)
    sms.add_student(student2)

    # Showing student details
    print(sms.show_student_details(1))  # Output: ID: 1, Name: Alice, Average Grade: 87.5

    # Showing student average grade
    print(sms.show_student_average_grade(2))  # Output: 77.5
