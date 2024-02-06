class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

class AttributeMixin:
    def to_dict(self):
        return self.__dict__

# Attach the Mixin feature to the Student class
class StudentWithAttributes(Student, AttributeMixin):
    pass

# Example usage:
student = StudentWithAttributes("Tornike", "Aphtsiauri", 29, "SKILLILL Neo-University")
print(student.to_dict())