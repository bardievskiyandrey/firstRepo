from datetime import datetime
import logging

from student import first_student

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", encoding="UTF-8")
class Student:
    print("Hi")

    def __init__(self, height=160, name="sasha", surname="aleksandrovich", birthdate="2000-12-12", zaklad="Akademiya shag", ocenka="12"):
        if(type(name) != str):
            raise TypeError(f"name must be str. Not a {type(name)}")
        if (type(surname) != str):
            raise TypeError(f"surname must be str. Not a {type(surname)}")
        if (type(birthdate) != str):
            raise TypeError(f"birthdate must be str. Not a {type(birthdate)}")
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        if birthdate > datetime.now():
            raise ValueError("birthdate cannot be in the future")
        if (type(height) != int):
            raise TypeError(f"height must be int. Not a {type(height)}")
        if height <= 0:
            raise TypeError("height cant be 0!")
        self.birthdate = birthdate
        self.height = height
        self.name = name
        self.surname = surname
        self.zaklad = zaklad
        self.ocenka = ocenka
        print("I am alive")
    def __bool__(self):
        return bool(self.zaklad)
    def __float__(self):
        return float(self.ocenka)
try:
    first_student = Student(180, "andrew", "andreyovich", "1990-07-10", "akademiya schag", 10)
    second_student = Student(220, "roma", "romanovich", "2006-01-11", "", 9)
    logging.info("programm started")
    logging.info(f"first student name: {first_student.name},first student surname: {first_student.surname}")
    logging.info(f"second student name: {second_student.name}, second student surname: {second_student.surname}")
    logging.debug("In progress...")
    logging.info("programm ended")
except (TypeError, ValueError) as error:
    logging.exception(error)
#print(first_student.height, first_student.name, first_student.surname, first_student.birthdate)
#print(second_student.height, second_student.name, second_student.surname, second_student.birthdate)
#print(bool(first_student))
#print(bool(second_student))
#print(float(first_student))
#print(float(second_student))