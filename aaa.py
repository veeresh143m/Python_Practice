# l=[1,2,3,7,9,10]
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1
# l=[1,2,3,7,9,10]
# list=len(l)
# for i in range(list):
#     print(l[i])
'''to display even and odd numbers'''
# for i in range(15):
#     if i%2==0:
#         print(i,'is even number')
#     else:
#         print(i,'is odd number')    
# def even_odd():
#     for n in range(20):
#       if n%2==0:
#           print(n,'is even')
#       else:
#           print(n,'is odd') 
# even_odd()
#                           '''factorial number'''
# n=int(input('Enter the number:'))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact,end=' ')
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#         print(fact)
# n=indt(input('Enter the number;'))
# fact(n)        
# def fibonacci(n):
#     a=0
#     b=1
#     fact=1
#     while fact<n:
#         print(a)
#         a,b=b,b+a
#         fact+=1
# n=int(input('Enter the number:'))
# fibonacci(n)
# string='honesty is the best polocy'
# wovels='aeiou'
# for s in string:
#     if s in wovels:
#         print(s,end='')    
   
'''reverse order of words'''
# s=input('Enter the str:')
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i-=1
# print(' '.join(l1))    
'''reverse internal content of each word'''
# s=input('Enter the string:')
# l=s.split()
# l1=[]
# l2=len(l)
# i=0
# while i<l2:
#     l1.append(l[i][::-1])
#     i+=1
# print(' '.join(l1))    
s=input('ENter the string:')
l=s.split()
l1=[]
i=len(l)-1
while 0<=i:
    l1.append(l[i])
    i-=1
print(l1)    




            

