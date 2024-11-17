import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", encoding="UTF-8")
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        logging.debug(f"animal created, name-{self.name}, age-{self.age}")

    def __str__(self):
       return f'|Animal|\nName : {self.name}\nAge : {self.age}\n'


class Fish(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def __str__(self):
        return f'|Fish|\nName : {self.name}\nAge : {self.age}\nSpeed: {self.speed}\n'

try:
    f = Fish("dory", 3, 10)
    print(str(f))
    logging.debug(f"name-{f.name}, age-{f.age}")
except (ValueError, NameError) as error:
    logging.error("Error :(")