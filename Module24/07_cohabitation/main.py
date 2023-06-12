import random

class Human:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.home = None

    def eat(self):
        if self.home.food >= 1:
            self.home.food -= 1
            self.hunger += 10
            print(f"{self.name} поел и теперь сытость равна {self.hunger}.")
        else:
            print(f"В доме нет еды для {self.name}!")

    def work(self):
        if self.hunger >= 10:
            self.hunger -= 10
            self.home.money += 50
            print(f"{self.name} поработал и заработал деньги, теперь в доме {self.home.money} денег.")
        else:
            print(f"{self.name} слишком голоден для работы!")

    def play(self):
        if self.hunger >= 5:
            self.hunger -= 5
            print(f"{self.name} поиграл и теперь сытость равна {self.hunger}.")
        else:
            print(f"{self.name} слишком голоден для игр!")

    def go_shopping(self):
        if self.home.money >= 10:
            self.home.money -= 10
            self.home.food += 20
            print(f"{self.name} сходил в магазин за едой и принес {self.home.food} еды в дом.")
        else:
            print(f"{self.name} не может позволить себе купить еду в магазине!")

    def roll_dice(self):
        return random.randint(1, 6)

    def act(self):
        if self.hunger < 0:
            print(f"{self.name} умер от голода!")
            return False
        dice_roll = self.roll_dice()
        if self.hunger < 20:
            self.eat()
        elif self.home.food < 10:
            self.go_shopping()
        elif self.home.money < 50:
            self.work()
        elif dice_roll == 1:
            self.work()
        elif dice_roll == 2:
            self.eat()
        else:
            self.play()
        return True

class Home:
    def __init__(self):
        self.food = 50
        self.money = 0

home = Home()
human1 = Human('Василий')
human1.home = home
human2 = Human('Мария')
human2.home = home


for i in range(365):
    print(f"День {i+1}")
    if not human1.act() and not human2.act():
        print("Оба человека умерли от голода!")
        break
    else:
        print('Все выжили!')