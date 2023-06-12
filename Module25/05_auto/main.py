import math
class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, distance):
        dx = distance * math.cos(self.direction)
        dy = distance * math.sin(self.direction)
        self.x += dx
        self.y += dy

    def turn(self, angle):
        self.direction += angle


class Bus(Car):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def get_on(self, num_passengers):
        self.passengers += num_passengers

    def get_off(self, num_passengers):
        self.passengers -= num_passengers

    def move(self, distance):
        super().move(distance)
        self.money += self.passengers * distance
