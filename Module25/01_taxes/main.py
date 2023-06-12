class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 500


money = float(input("Введите количество денег: "))
property_worth = float(input("Введите стоимость имущества: "))

tax = 0
if property_worth > 0:
    apartment = Apartment(property_worth)
    tax += apartment.calculate_tax()

    car_worth = property_worth / 2
    car = Car(car_worth)
    tax += car.calculate_tax()

    country_house_worth = property_worth / 4
    country_house = CountryHouse(country_house_worth)
    tax += country_house.calculate_tax()

if money >= tax:
    print(f"Налог на имущество составляет {tax:.2f}.")
    print(f"У вас осталось {money - tax:.2f} денег.")
else:
    print("У вас недостаточно денег для оплаты налога на имущество.")
