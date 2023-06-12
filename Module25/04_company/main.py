class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def calculate_salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, first_name, last_name, age, sales):
        super().__init__(first_name, last_name, age)
        self.__sales = sales

    def get_sales(self):
        return self.__sales

    def calculate_salary(self):
        return 5000 + 0.05 * self.__sales


class Worker(Employee):
    def __init__(self, first_name, last_name, age, hours_worked):
        super().__init__(first_name, last_name, age)
        self.__hours_worked = hours_worked

    def get_hours_worked(self):
        return self.__hours_worked

    def calculate_salary(self):
        return 100 * self.__hours_worked
employees = [
    Manager("Иван", "Иванов", 35),
    Manager("Петр", "Петров", 40),
    Manager("Сидор", "Сидоров", 45),
    Agent("Анна", "Аннова", 25, 100000),
    Agent("Борис", "Борисов", 30, 200000),
    Agent("Виктория", "Викторова", 35, 300000),
    Worker("Григорий", "Григорьев", 20, 120),
    Worker("Дмитрий", "Дмитриев", 25, 150),
    Worker("Екатерина", "Екатеринова", 30, 180),
]
for employee in employees:
    print(f"{employee.get_first_name()} {employee.get_last_name()}: {employee.calculate_salary()} рублей")
