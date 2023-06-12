from functools import reduce
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats1 = [round(x ** 3, 3) for x in floats]
print(floats1)

names2 = list(filter(lambda x: len(set(x)) >= 5, names))
print(names2)

numbers1 = reduce(lambda prev, el: prev * el, numbers)
print(numbers1)