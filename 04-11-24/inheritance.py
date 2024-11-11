class Animal:
    def __init__(self, name,age ):
        self.name = name
        self.age = age
    def __str__(self):
        return f"|animal|\nName:{self.name}\nAge:{self.age}\n"
class Fish(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed
    def __str__(self):
        return f"|fish|\nName:{self.name}\nAge:{self.age}\n"
f = Fish("dory", 3 , 10)
print(str(f))
