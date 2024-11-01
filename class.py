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
        if self.car.drive == True:
            self.job = Job(jobs)
        else:
            self.repair()
    def gethome(self):
        if self.home is None:
            self.home = Home()
    def getcar(self):
        if self.car is None:
            self.car = Car(brands)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            self.home.food -= 1 and self.satiety + 5
    def work(self):
        if self.car.drive == True:
            self.money += self.job.salary and self.happines - 5 and self.satiety - 5
        else:
            self.repair()
    def shopping(self, manage):
        if manage == "food":
            self.money -= 10 and self.home.food + 10
        if manage == "fuel":
            self.money -= 50 and self.car.fuel + 25
        if manage == "delicious":
            self.money -= 25 and self.satiety + 20
    def chill(self):
        self.happines += 10 and self.home.mess + 5
    def clean(self):
        self.happines -= 5 and self.home.mess == 0
    def repair(self):
        self.car.strength += 100 and self.money - 50
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



