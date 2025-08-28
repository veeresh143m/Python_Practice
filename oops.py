# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print('name:',self.name)    
#         print('age:',self.age) 
#         print('marks:',self.marks) 
# s=student('veeresh',21,99.9)
# s.display()        
'''we can call method ,how many times and result also exicuted that 
times, but constructor only one time exicuted'''
# class teacher:
#     def __init__(self):
#         print('my name is veeresh')
#     def m1(self):
#         print('what is your name')
# t=teacher()
# t.m1() #method two times call and two times exicuted but, construnctor only one time exicuted
# t.m1()     
'''create a list of objects in constructor'''
   
# class Movie:
#     def __init__(self, name, hero, rating):   # constructor should be __init__
#         self.name = name
#         self.hero = hero
#         self.rating = rating

#     def method(self):
#         print(self.name)
#         print(self.hero)
#         print(self.rating)

# movies = [  # better variable name
#     Movie('rrr', 'ram', 4.5),
#     Movie('sitaramam', 'ds', 4.5),
#     Movie('pushpa', 'aa', 4.0)
# ]

# for movie in movies:   # iterate over the list
#     movie.method()
#     print('-------')
# class Movie:
#     def __init__(self,name,rating):
#         self.name=name
#         self.rating=rating
#     def method(self):        
#         print(self.name)
#         print(self.rating)
# m=[
#     Movie('rrr',4.5),
#     Movie('sitaramam',4.5)
# ]  
# for Movie in m:
#     Movie.method()
#     print('------------------')            
'''inheritance'''
'''single inheritance'''
# class student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def m1(self):
#         print(self.a)
#         print(self.b)
#         print('this is student method')
# class teacher(student):
#     def m2(self):
#        print('this is teacher method')
# t=teacher(9,99)
# t.m1()
# t.m2()
# class P:
#     def m1(self):
#         print('this is parent method')
# class S(P):
#     def m2(self):  
#         print('this is student method')
# s=S()
# s.m1()
# s.m2()              
'''multiple inhertance'''
# class teacher:
#     def m1(self):
#         print('this is teacher method')
# class studnet(teacher):
#     def m2(self):
#         print('this is studnet method')       
# class parent(studnet):
#     def m3(self):
#         print('this is parent method')
# p=parent()
# p.m1()
# p.m2()
# p.m3()    
'''hierarchical inheritance'''
# class c:
#     def m1(self):              
#         print('this is c method')
# class p(c):
#     def m2(self):
#         print('this is parent method')
# class p1(c):
#     def m3(self):
#         print('this is p1 method')
# parent=p()
# parent.m1()
# parent.m2()
# parent1=p1()
# parent1.m3()
# parent1.m1()
'''multiple inheritance'''
# class p:
#     def m1(self):
#         print('this is p method')
# class c:
#     def m2(self):   
#         print('this is c method')
# class pc(p,c):
#     def m3(self):
#         print('this is pc method')
# abc=pc()
# abc.m1()
# abc.m2()
# abc.m3()                             

