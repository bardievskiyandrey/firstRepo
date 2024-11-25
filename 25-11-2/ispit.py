class Temperature:
    def __init__(self, temperature:float, unit:str):
        units = ("K", "C", "F")
        if unit not in units:
            raise NameError(f"wrong unit! unit cant be {unit}")
        if unit == "K" and temperature < 0:
            raise ValueError("Kelvin temperature cant be 0!")
        if unit == "C" and temperature < -273.15:
            raise ValueError("celsius temperature cant be bellow -273.15!")
        if unit == "F" and temperature < -459.67:
            raise ValueError("fahrenheit temperature cant be bellow -459.67!")
        self.temperature = temperature
        self.unit = unit
    def to_kelvin(self):
        if self.unit == "K":
            raise ValueError("temperature already in kelvin")
        if self.unit == "C":
            self.temperature += 272.15
            self.unit = "K"
        if self.unit == "F":
            self.temperature += 457.87
            self.unit = "K"
    def to_celsius(self):
        if self.unit == "C":
            raise ValueError("temperature already in celsius")
        if self.unit == "K":
            self.temperature -= 272.15
            self.unit = "C"
        if self.unit == "F":
            self.temperature = (self.temperature-32)*5/9
            self.unit = "C"
    def to_fahrenheit(self):
        if self.unit == "F":
            raise ValueError("temperature is already in fahrenheit")
        if self.unit == "K":
            self.temperature = (self.temperature-273.15)*9/5+32
            self.unit = "F"
        if self.unit == "C":
            self.temperature = (self.temperature*9/5)+32
            self.unit = "F"
    def __str__(self):
        return f"temperature:{self.temperature} unit:{self.unit}"
try:
    temperature = Temperature(21, "C")
    print(temperature)
except (ValueError, NameError) as error:
    print("error")