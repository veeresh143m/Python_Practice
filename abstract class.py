# from abc import*
# class vehicle(ABC):
#     @abstractmethod
#     def no_of_wheels(self):
#         pass
# class bus(vehicle):
#     def no_of_wheels(self):
#         return 4
# class auto(vehicle):
#     def no_of_wheels(self):
#         return 3
# b=bus()
# print(b.no_of_wheels())  
# a=auto()
# print(a.no_of_wheelsform )
'''from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class manager(Employee):
    def salary(self):
        print('the manager salary is 5000')
class developer(Employee):
    def salary(self):
        print('the developer salary is 4000')
m=manager()
m.salary()
d=developer()
d.salary()'''

from abc import*
class employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class manager(employee):
    def salary(self):
        print('the manager salary is 100000')
class developer(employee):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a)
        print(self.b)
    def salary(self):
        print('the developer salary is 120000')
m=manager()
m.salary()
d=developer(12,34)
d.salary()
d.display()
    
















    
    
