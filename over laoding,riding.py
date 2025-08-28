# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def m1(self,a,b):
#         print('this is m1 method',a,b)
#     def m2(self,a,b,c): 
#         print('this m2 method',a,b,c)
#     def m3(self):
#         print(self.name)
#         print(self.age)
#         print('this is m3 method')
# s=student('veeresh',21)
# s.m3()
# s.m2(1,3,2)
# s.m1(1,2)
# class student:
#     def m1(self,a,b):
#         print('this is m1 method',a,b)
#     def m2(self,a,b,c,d):
#         print('this si m2 method')
#     def m3(self,a,b,c):
#         print('this is m3 method',a,b,c)
# s=student()
# s.m3(10,20,30)    
''' method over loading'''
# class test:
#     def m3(self):
#         print('this is my method ')
#     def m3(self,a,b):
#         print('this is second method')
#     def m3(self,a,b,c):
#         print('this si third method',a,b,c)
# t=test()
# t.m3(20,10,20)     
'''constructor overloading'''
# class test:
#     def __init__(self,a,b):
#         print(a,b)
#     def __int__(self,a):
#         print(a)
#     def __init__(self,a,b,c):
#         print('this si last constructor',a,b,c) 
# t=test(10,20,30)                         