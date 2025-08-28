# '''append,extend,remove,index,count,pop,insert,len'''
# a=[1,2,3,4]
# a.append(5)
# print(a)
# b=[1,2,3,4]
# c=[5,6,7,8]
# b.extend(c)
# print(b)
# print(len(a))
# c.remove(6)
# print(c)
# a.pop(3)
# print(a)
# a.insert(2,23)
# print(a)
# a[2]=33
# print(a)
# a=[9,6,1,3,7]
# a.sort()
# print(a)
# '''tuple,index,len,count,min,max,sort'''
# a=1,2,3
# print(type(a))
# a=(1,10,40,20,30)
# print(min(a))
'''to get the first letter'''
# a=['ram','sita','hanuma','lakshmana']
# b=[x[0] for x in a] 
# print(b)
# words=['abc','bcde','xyz']  
# l=[[x[0],x.upper()] for x in words]  
# print(l)    
# l=[[x[0],len(x)] for x in words]  
# print(l) 
# l=[i*i for i in range(1,11)]
# print(l)
# a=int(input('enter the number:'))
# for i in range(1,11):
#     print(a,'*',i,'=',i*a)

# l=[]
# for i in range(1,11):
#     l.append(i*i)
#     print(l)
# l=input('Enter the searching word:')
# vowels=['a','e','i','o','u']
# found=[]
# for letter in l:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# print(found)  
# word=input('enter the word')
# s=set(word)
# v={'a','e','i','o','u'} 
# d=s.intersection(v)     
# print(d)    
# l=input('enter the list:')
# a=set(l)
# w=['a','i','o','u','e'] 
# t=a.intersection(w) 
# print(t)    
# def add(a,b):
#     return a+b
# a=add(20,30)
# print(a)
# def total(a,b):
#     return a+b,a-b,a*b,a/b
# t=total(20,5)
# print(t)
# def number():
#     for i in range(1,10):
#         print(i)
# number()  

# def n():
#     a=1
#     while a<=10:
#         print(a,end=' ')
#         a+=1
# n()   
# def n():
#     nk=int(input("Enter any number:"))
#     num=1
#     while num<=nk:
#         if num%2==0:
#             print(f"{num} this is even number") 
#         else:
#             print(f"{num} this is odd number")  
#         num+=1      
# n()                     
# def list():
#     l=[1,2,3,'veeresh',22]
#     i=0
#     while i<len(l):
#         print(l[i],i)
#         i+=1
# list()


# def list():
#     l=[1,2,3,4]
#     i=len(l)-1
#     while i>=0:
#         print(l[i])

#         i-=1
# list()        
# def str(n): 
#     i=1
#     emt=[]
#     while i<=len(n):
#         b=(n[-i])
#         emt.append(b)
#         i+=1
#     print(emt)
# n=input('Enter the name:')
# def str(n): 
#     i=1
#     while i<=len(n):
#         b=(n[-i])
#         print(b)
#         i+=1
# n=input('Enter the name:')
# str(n)        


# n=input('Enter the name:')
# i=0
# while i<len(n):
#     print(n[i])
#     i+=1
# n=input('Enter the name:')
# i=0
# while i<len(n):
#     print(n[-i])
#     i+=1
# n=input('enter the name:') 
# i=0
# while i<len(n):
#     print(n[i])
#     i+=1   
# l=[10,20,'veeresh','hi']
# a=len(l)
# i=0
# while i<a:
#     print(l[i],end='')
#     i+=1
# t=('hi','bye','hello')
# i=0
# while i<len(t):
#     print(t[i],end=' ')
#     i+=1
# l=[1,'hi',2,'bye']
# for i in l[1]:
#     print(i)
# l=[1,'hi',2,'bye']
# for i in l[::-1]:
#     print(i)
# n=int(input('enter the number:'))
# for i in range(n):
#     if i%2==0:
#         print('even number',i)
#     else:
#         print('odd number',i)    
# def n(*add,n1):
#     print(sum(add),n1)
# n(1,2,3,4,5,6,n1='hello veeresh')    
# def f1(*s,n1):
#     for i in s:
#         print(i,n1)
# f1(1,2,3,4,n1=300)        
# list=[1,2,3,4]
# list.insert(2,1000)
# print(list)
# x=[1,2,3,4]
# y=x
# y[1]=999
# print(y)
# print(x)
# x=[1,2,3,4]
# y=x.copy()
# y[1]=1000
# print(x)
# print(y)

#def fact(n):
#     fact=1
#     while n>fact:
#         print(fact)
#         fact*=fact
# n=int(input('Enter the number:'))            
# fact(n)        
# a=20
# for i in range(1):
#     while a>=i:
#        i+=1
#        print(i)
# n=int(input("Enter any number:"))
# p=1  #9   12 3 3
# a=1
# while a<=n:
#     p*=a
#     a+=1
# print(p)
#def fact(n):
#     fact=1
#     while n>fact:
#         print(fact)
#         fact*=fact
# n=int(input('Enter the number:'))            
# fact(n)     


# n=int(input('Enter the number:'))
# value=1
# a=1
# while a<=n:
#     value+=a
    
#     a+=1
# print(value)
# n=int(input('Enter the number:'))
# i=1
# a=1
# while i<=n:
#     a*=i
#     print(a)
#     i+=1
# a=input('Enter the numenr:')
# b=len(a)
# for i in range(b):
#     print(a[i])
# a='hello'
# for i in range(len(a)-1,-1,-1):
#     print(a[i],end=' ')
# a='ramasita'
# r=''
# for i in a:
#     r=i+a
# print(r)    
# a=int(input('Enter the number:'))
# fact=1
# for i in range(1,a):
#     fact*=i
#     print(fact)
# a=int(input('Enter the number::'))
# fact=1
# value=1
# while value<=a:
#     fact*=value
#     print(fact)
#     value+=1
# a=int(input('Enter the number:'))
# for i in range(1,a+1):
#     print('------------')
#     for j in range(1,11):
        
#         print(i,'*',j,'=',i*j)
# a=int(input('Enter the number:'))
# i=1
# while i<=a:
#     j=1
#     print('------------')
#     while j<=10:
#         print(i,'*',j,'=',i*j)
#         j+=1
#     i+=1    

# list_items=[1,2,1,4,2,5,1,3,6,7,5,7]
# items=list(set(list_items))
# print(items)

# list_i=[1,2,3,4,1,2,3,4,5,6,7,5,8]
# li=[]
# for i in list_i:
#     if i not in li:
#         li.append(i)
#         print(li)

# def fibo(n):
#     a=0
#     b=1
#     i=0
#     while i<n:
#         print(a)
#         a,b=b,b+a
#         i+=1
# n=int(input("Enter the number:"))
# fibo(n)     
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         r=n+sum(n-1)
#         return r
# a=sum(6)
# print(a)       
# str='veeresh ramu' 
# a='aeiou'
# for s in str:
#     if s in a:
#         print(s,end=' ')

# str='veeresh kumar roy'
# v='aeiou'
# for chr in str:
#     if chr not in v:
#         print(chr,end=' ')
# list=[1,2,3,1,4,52,6,7,9,3,6]
# li=[]
# for i in list:
#     if i not in li:
#         li.append(i)
# print(li)
# n=[2,10,1,4,2,3,9]
# lst=n[:]
# while lst:
#     m=min(lst)
#     print(m,end=' ')
#     lst.remove(m)
# l=[10,2,33,9,13]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[j]<l[i]:
#             l[i],l[j]=l[j],l[i]
# print(l)            
# s=input('Enter the string:')
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i-=1
# print(l1)    
# def square(n):
#     return n*n
# for i in range(1,8):
#     print(f'the square of {i} is {square(i)}')
# l=[20,1,4,7,2,80,4,60,7]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l) 
'''sum of list elements'''           
# l=[1,2,3,4,5]
# total=0
# for i in l:
#     total+=i
# print(total)
# def max_min_num(li):
#     max = li[0]
#     for i in li:
#         if i > max:
#             max = i
#     print(max)

#     min = li[0]
#     for i in li:
#         if i < min:
#             min = i
#     print(min)

# max_min_num([1,88,9,55,4,885])
# n=[20,40,10,90,30]
# max=n[0]
# for i in n:
#     if i>max:
#         max=i
#     print(max)   
l=[100,20,10,40,60]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[j],l[i]=l[i],l[j]
# print(l)   







