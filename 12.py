import random
import cv2
class dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.saturation = 40
        self.weight = 20
        self.alive = True
    def to_eat(self):
        print("Time to eat")
        self.saturation += 2
        self.weight += 0.10
        self.gladness += 1
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 2
        self.weight += 0.1
    def to_chill(self):
        print("Rest time")
        self.gladness += 1
        self.saturation -= 2
        self.weight += 0.1
    def to_walk(self):
        print("I will walk")
        self.gladness += 1
        self.saturation -= 5
        self.weight -= 0.50
    def is_alive(self):
        if self.weight < 10:
            print("Death from starvation")
            self.alive = False
        elif self.saturation == 0:
            print("Death from starvation")
            self.alive = False
        elif self.gladness == 0:
            print("Depression…")
            self.alive = False
        elif self.weight >= 30:
            print("Death from overeating")
            self.alive = False
        elif self.weight <= 20:
            print("Normal weight…")
            self.alive = False
        elif self.gladness >= 500:
            print("Normal gladness")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"saturation = {round(self.saturation, 2)}")
        print(f"Weight = {round(self.weight, 2)}")
    def end_of_year(self):
        if day == "364":
            print(f"Gladness = {self.gladness}")
            print(f"saturation = {round(self.saturation, 2)}")
            print(f"Weight = {round(self.weight, 2)}")
        breakpoint()
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
snikers = dog(name="snikers")
for day in range(365):
 if snikers.alive == False:
    break
 snikers.live(day)
a = input("???")

if a == "???":
    print("file:///C:/Users/student/Downloads/image.jpeg")
else:
    print("NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
