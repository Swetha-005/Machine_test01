class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_role(self):
        print("I am a person")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_role(self):
        print("I am a student")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_role(self):
        print("I am a teacher")

class Principal(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def display_role(self):
        print("I am the principal")


student = Student("SWETHA", 22, "BTech")
teacher = Teacher("Preetha", 35, "computer Programming")
principal = Principal("Anagha", 50, "CUCEK")


print(student.name, student.age, student.grade)
student.display_role()

print(teacher.name, teacher.age, teacher.subject)
teacher.display_role()

print(principal.name, principal.age, principal.school)
principal.display_role()
