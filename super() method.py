# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def m1(self):
#         print('this is m1 method')
# class teacher(student):
#     def __init__(self,name,marks,age,salary):
#         super().__init__(name,marks)
#         self.age=age
#         self.salary=salary
#     def m2(self):
#         print(self.name)
#         print(self.marks)
#         print(self.age)
#         print(self.salary)
#         print('this is m2 method') 
#         super().m1()
# t=teacher('veeresh',99,21,200000)
# t.m2() 
#                       
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def m1(self):
#         print(self.name)
#         print(self.age)
# class teacher(student):
#     def m2(self):
#         print('hello students')
#         super().m1()
# t=teacher('veeresh',21)
# t.m2()

# class id:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def m1(self):
#         print('this is m1 method')
# class sub_id(id):
#     def __init__(self,name,marks,age,avg):
#         super().__init__(name,marks)
#         self.age=age
#         self.avg=avg
#     def m2(self):
#         print(self.name)
#         print(self.marks)
#         print(self.age)
#         print(self.avg)
#         print('this is m2 method')
#         super().m1()
# s=sub_id('veeresh',100,21,99.0)
# s.m2()                        
        