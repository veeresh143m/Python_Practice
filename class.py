# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.marks)   
# s=student('veeresh',21,999)
# s.display()      
# class movie:
#     def __init__(self,name,hero,rating):
#         self.name=name
#         self.hero=hero
#         self.rating=rating
#     def info(self):
#         print('movie name:',self.name)    
#         print('hero name:',self.hero)  
#         print('movie rating:',self.rating) 
# movies=[
#         movie('rrr','ramcharan',5),
#         movie('sitaramam','dulkhar',4.5),
#         movie('saho','prabhas',4)
#         ] 
# for movie in movies:
#     movie.info()        

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         print('this a m1 method')  
#         self.c=30
#         self.d=40
# t=test()
# print(t.__dict__)  
# t.m1()  
# print(t.__dict__)  
'''access the instant variable in method'''    
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#     def m1(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)    
# t=test()
# print(t.__dict__)
# t.m1()   
# import random
# a=[1,2,3,4]
# b=random.choice(a)
# print(b)
# n=9
# print("* " * n)
# for i in range(n-2):
#     print("*"+"  "*(n-2)+" *")
# print("* " * n)
# a=[1,2,3,4]
# b=a.copy()
# a[1]=200
# print(a)
# print(b)
# a='sita'
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1
# b='rama'
# c=len(b)-1
# while c>=0:
#     print(b[c])
#     c-=1   
# l=[1,2,3,4,5]
# i=len(l)
# b=0
# while b<i:
#     print(l[b])
#     b+=1

# b='rama'
# c=len(b)-1
# while c>=0:
#     print(b[c])
#     c-=1

# b='rama'
# s=[]
# for i in b:
#     s.insert(0,i)
# print(s,end="")
# a='rajaram'
# b=[]
# for i in a:
#     b.insert(0,i)
#     print(b)
# a='ramanujan'
# b=len(a)
# for i in range(b):
#     print(a[i])
# a='ramanujan'
# for i in a[::-1]:
#     print(i)
# a='sitarama'
# l=[]
# for i in a:
#     l.insert(0,i)
# print(l)
# n=int(input('Enter the number:'))
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     print(fact)
#     i+=1
# n=int(input('Enter the number:'))
# a=0
# b=1
# count=0
# while count<n:
#     print(a)
#     a,b=b,b+a
#     count+=1
# def odd_even(n):
    
#  for i in range(0,n):
#     if i%2==0:
#         print(f"{i}, is even number")
#     else:
#         print(f"{i} ,is odd number") 
# n=int(input('Enter the nuber:'))        
# odd_even(n)           
# li=[1,2,3,4,1,2,5,6,6,5,8,4]
# l=list(set(li))
# print(l)
# m=[1,2,3,1,2,3,4,5,2,3,6,7]
# li=[]
# for item in m:
#     if item not in li:
#         li.append(item)
#     print(li)

# n=int(input('Enter the number:'))
# a=0
# b=1
# count=0
# while count<n:
#     print(a)
#     a,b=b,b+a
#     count+=1
# n=int(input("enter the number:"))
# a=0
# b=1
# i=0
# while i<n:
#     print(a)
#     a,b=b,b+a
#     i+=1
    






