
class Student:
    print("Hi")

    def __init__(self, height=160, name="sasha", surname="aleksandrovich", birthdate="2000-12-12"):
        self.height = height
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        print("I am alive")
first_student = Student(186, "andrew", "andreyovich", "1990-07-10")
second_student = Student(220, "roma", "romanovich", "2006-01-11")
print(first_student.height, first_student.name, first_student.surname, first_student.birthdate)
print(second_student.height, second_student.name, second_student.surname, second_student.birthdate)