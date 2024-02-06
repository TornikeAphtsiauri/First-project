class Student:
    def __init__(self, name, grade, age):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(grade, int) or not (0 <= grade <= 100):
            raise ValueError("Grade must be an integer between 0 and 100")
        if not isinstance(age, int) or not (18 <= age <= 99):
            raise ValueError("Age must be an integer between 18 and 99")

        self.name = name  # instance attribute
        self.grade = grade  # instance attribute
        self.age = age  # instance attribute

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer")
        if amount <= 0:
            raise ValueError("Amount must be a positive integer")

        self.grade += amount

    def __str__(self):
        return f"Student: name: {self.name}, grade: {self.grade}, age: {self.age}, is_passing: {self.is_passing}"


# Creating an instance of the Student class
student1 = Student("Tornike", 85, 29)
print(student1)  # Output: Student: name: Tornike, grade: 70, age: 29, is_passing: True

# Increase grade by 10
amount = int(input("Enter amount to increase grade: "))
student1.increase_grade(amount)
print(student1)  # Output: Student: name: Tornike, grade: 80, age: 29, is_passing: True
