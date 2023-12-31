from typing import Iterable


class SquaresNumbers:
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__first_elem = 0
        self.__counter = 0

    def __iter__(self):
        self.__first_elem = 0
        self.__counter = 0
        return self

    def __next__(self) -> int:
        self.__counter += 1
        if self.__limit <= 0:
            raise StopIteration
        elif self.__limit >= 1:
            if self.__counter > self.__limit:
                raise StopIteration
        self.__first_elem += 1
        return self.__first_elem * self.__first_elem


def square_func(nums: int) -> Iterable[int]:
    for num in range(1, nums + 1):
        yield num ** 2


number_user = int(input('Введите число от 1 до N: '))
squares_numbers = SquaresNumbers(limit=number_user)

print('\nКласс-итератор')
for num_i in squares_numbers:
    print(num_i, end=' ')

print('\n\nФункция генератор')
for x in square_func(number_user):
    print(x, end=' ')

print('\n\nГенераторное выражение')
square_gen = (num ** 2 for num in range(1, number_user + 1))
for i_num in square_gen:
    print(i_num, end=' ')
