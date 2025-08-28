# s=input('Enter the string:')
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i-=1
# print(' '.join(l1))    
# s=input('Enter the string:')
# l=s.split()
# l1=[]
# i=0
# while i<len(l):
#     l1.append(l[i][::-1])
#     i+=1
# print(' '.join(l1))   
# s=input('Enter the string:')
# l=s.split()
# l1=[]
# for i in l:
#     l1.append(i[::-1])
# print(' '.join(l1))   
# num=int(input('Ente the number:'))
# n=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**n
#     temp//=10
# if num==sum:
#     print(sum)
# else:
#     print('not match')    
# s=int(input('Enter the number:'))
# fact=1
# for i in range(1,s):
#     fact*=i
# print(fact,end=' ')
# s=int(input('Enter the number:'))
# fact=1
# value=1
# while fact<=s:
#     value*=fact
#     fact+=1
#     print(value)
# s='veeresh'
# for i in s:
#     print(i)
# s='veeresh'
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end=' ')
# s='veeresh'
# i=0
# while i<len(s):
#     print(s[i],end=' ')
#     i+=1
# s='veeresh'
# i=len(s)-1
# while i>=0:
#     print(s[i],end='')
#     i-=1
# for i in range(1,20):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
# for i in range(1,20):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
# n=int(input('Enter the nuber:'))
# for i in range(1,n):
#     if i>0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=' ')    
# from faker import Faker
# from random import*
# fake=Faker()
# for i in range(6):
#     print({
#         'name':fake.name(),
#         'age':randint(20,37),
#         'mail':fake.email()
#     })
