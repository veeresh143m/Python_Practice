# n=int(input('Enter the number: '))
# if n%2==0:
#     print(n,'this number is even_number')
# else:
#     print(n,'this number is odd number')    

# from faker import Faker
# faker=Faker()
# for i in range(5):
#     print({
#         'name':faker.name(),
#         'emai':faker.email(),
#         'phone_number':faker.phone_number()

#     })

# list=[10,20,30,50]
# n=len(list)+1
# exp_value=n+(n+1)//2
# act_value=sum(list)
# total_value=act_value-exp_value
# print(total_value)

# gen=input('Enter the gender:')
# age=int(input('Enter the age:'))
# if gen=='m':
#     print('this is male information')
#     if age>=21:
#         print('now your eligible and use the vote')
#     else:
#         print('your not eligible because your age is:',age)
# elif gen=='f':
#     print('this is female information')      
#     if age>=20:
#         print('ok your also eligible') 
#     else:
#         print('your not eligible because your age is:',age)  
# else:
#     print('please provide correct gender male/famale') 

# class student:              
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def display(self):
#     print(self.name)
#     print(self.age)
# d=student('veeresh',21)
# d.display()
# class teacher:
#     def __init__(self,age,name):
#         self.age=age
#         self.name=name
# t=teacher(23,'krishna')   
# print(t.age)
# print(t.name)     
# n=int(input("enter the number:"))
# a=0
# b=1

# for i in range(n):
#     print(a,end=" ")
#     a=b
#     b=a+b
'''fibonacce series'''
# n=18
# a,b=0,1
# for i in range(n):
#     print(a,end=' ')
#     a,b=b,b+a
'''factorial series'''
# n=5
# fact=1
# for i in range(1,n+1):
    
#     fact*=i
#     print(fact,end=' ')
# fact=1
# for i in range(1,10):
#     fact*=i
#     print(fact,end=' ')
# a=20
# for i in range(1,a+1):
#     if i%2!=0:a.update({4:40})
# print(a)

#         print(i)
   
# a=input("Enter the string:")
# ab=input("Enter the another string")
# if ab in a:
#     print('yes this string in a and ab')
# else:
#     print('no this string is not in ab') 
# a=int(input('Enter the number:'))
# b=int(input('enter the number:'))
# if a==b:
#     print('yes this number is same as')   
# else:
#     print('not match') 
   
# import pickle
# l=['rama',123,'sita']
# with open('data.txt','wb') as f:
#     pickle.dump(l,f)
# a=open('data.txt','rb') 
# b=pickle.load(a)   
# print(b)


# a={1:2,3:4,5:5}
# b={6:7,8:9,10:9}
# a.update(b)
# print(a)

# a={1:1,2:2,3:3}
# a.update({4:4})
# print(a)

# a={1:1,2:20,3:3,4:4}
# b=a.keys()
# print(b)

# a={1:2,3:4,4:5,6:7}
# print(a.keys())

# a={1:20,3:40,4:58,6:97}
# b=a.pop(3)
# print(b)
# a={1:1,2:22,3:3}
# b=a.get(2)
# print(b)
'''armstrong number'''
# n=int(input("Enter the number:"))
# a=n

# power=len(str(n))
# total=0
# for digits in str(a):
#    d=a%10
#    total+= d**digits
# if total==a:
#     print('armstrong number')
# else:
#     print('this is not armstrong number') 
   
# n=18
# a,b=0,1
# for i in range(n):
#     print(a,end=' ')
#     a=b
#     b=b+a
'''fibonacci series'''
# n=18
# a,b=0,1
# for i in range(n):
#     print(a,end=' ')
#     a,b=b,b+a
'''factorial'''
# a=6
# fact=1
# for i in range(1,a):
    
#     fact*=i
#     print(fact)
# n=int(input('Enter the number:'))
# fact=1
# for i in range(fact,n):
#     fact*=i
#     print(fact)
# n=int(input('Enter the number:'))
# fact=1
# value=1
# while fact<=n:
#     value*=fact
#     print(value)
#     fact+=1
# n=10
# a=1
# f=1
# while a<=n:
#     f*=a
#     print(f)
#     a+=1
# n=7
# a=1
# for i in range(a,n):
#     a*=i
#     print(a)

# def fact(n):
#     a=1
#     f=1
#     while a<=n:
#         f*=a
#         print(f)
#         a+=1
# n=int(input("Enter the nuber:"))
# fact(n)     
# def str(s):
#     a=len(s)
#     i=0
#     while i<a:
#         print(s[i])
#         i+=1
# s=input('Enter srt:')
# str(s)              
# def str(s):
#     i=len(s)-1
#     while  i>=0:
#         print(s[i])
#         i-=1
# s=input('str')
# str(s)
# a=10
# for i in range(11):
#     print(a,'*',i,'=',a*i)
# a=int(input('enter number:'))
# i=1
# while i<a:
#     print(a,'*',i,'=',i*a)
#     i+=1  
# a=int(input('enter number:'))
# for i in range(1,a+1):
#     for j in range(1,13):
#         print(i,'*',j,'=',i*j)
a=int(input('Enter the number:'))
i=1

while i<=a:
    j=1
    while j<=10:
       print(i,'*',j,'=',i*j)
       j+=1
    print() 
    i+=1    
        