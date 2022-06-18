# a = 0
# for i in range(4):
#     for j in range(i):
#         a += 1
#
#         print(a, end=" ")
#     print()

from abc import ABC, abstractmethod


# class Car():
#     def mil(self):
#         pass
#
#
# class Tesla(Car):
#     def mil(self):
#         print("The mileage is 30kmph")
#
#
# class Suzuki(Car):
#     def mil(self):
#         print("The mileage is 25kmph ")
#
#
# class Duster(Car):
#     def mil(self):
#         print("The mileage is 24kmph ")
#
#
# class Renault(Car):
#     def mil(self):
#         print("The mileage is 27kmph ")
#
#     # Driver code
# t = Tesla()
# t.mil()

class PhoneNumber():
    def __init__(self, area_code, number) -> None:
        self.area_code = area_code
        self.number = number

    def display(self):
        print(f'({self.area_code}) {self.number}')


pn = PhoneNumber('973', '555-1234')
pn.display()



