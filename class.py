import random
class Human:

    def __init__(self, name="human", job=None, home = None, car=None):
        self.name = name
        self.job = job
        self.money = 100
        self.happines = 50
        self.satiety = 50
        self.home= home
        self.car = car
    def getjob(self):
        pass
    def gethome(self):
        pass
    def getcar(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shoppint(self, manage):
        pass
    def chill(self):
        pass
    def clean(self):
        pass
    def repair(self):
        pass
    def daysindex(self, day):
        pass
    def isalive(self):
        if (self.happines < 0):
            print(f"{self.name} has depression...")
            return False
        if(self.satiety < 0):
            print(f"{self.name} is dead...")
            return False
        if (self.money < -500):
            print(f"{self.name} is bankrupt...")
            return False
        return True
    def live(self):
        pass
class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consuption = brand_list[self.brand]["consuption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consuption:
            self.fuel -= self.consuption
            return True
        else:
            print("Car cannot move")
            return False
class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0
class Job:
    def __init__(self, jobs):
        self.job = random.choice(list(jobs))
        self.salary = jobs[self.job]["salary"]
        self.gladness = jobs[self.job]["gladness"]
jobs = {
    'Java developer':{"salary":50, "gladness":10,},
    'Python':{"salary":100, "gladness":10,},
    'C++':{"salary":100, "gladness":5,},
    'Rust':{"salary":50, "gladness":3,},

}
brands = {
    'BMW':{"fuel":100, "strength":100, "consuption":6},
    'Volvo':{"fuel":200, "strength":150, "consuption":20},
    'Ferari':{"fuel":80, "strength":120, "consuption":8}
}
first_car = Car(brands)



