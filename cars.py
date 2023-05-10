from turtle import Turtle
import random
COLORS = ['orange', 'green', 'blue', 'red', 'pink', 'yellow', ]
Y_RANGE = range(-240, 260)
X_RANGE = range(-295, 260)
START_MOVE = 5
MOVE_INC = 1



class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = [] #can use list from main because is class attribute
        self.hideturtle()
        self.car_speed = START_MOVE


    def move(self):
        for i in self.cars:
            i.backward(self.car_speed)

    def gen_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1.2, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(270, random.choice(Y_RANGE))
            self.cars.append(new_car)

    def speed_up(self):
        self.car_speed += MOVE_INC






