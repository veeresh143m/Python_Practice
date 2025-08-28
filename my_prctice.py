# s='veeresh'
# rev=' '.join(reversed(s))
# print(rev)
# n=int(input('Enter the number:'))
# for i in range(n):
#     if i%2==0:
#         print(i,'is even number')
#     else:
#         print(i,'is odd number')      
# a=10
# b=20
# a,b=b,a
# print(a,b)
# n=int(input('Enter the number:'))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     a,b=b,b+a
# n=int(input('Enter the number:'))
# a=0
# b=1
# count=0
# while count<n:
#     print(a)
#     a,b=b,b+a
#     count+=1
# n=input('Enter the str:') 
# rev=''
# for i in n:
#     rev=i+rev
# if n==rev:
#     print(n,'this is palindrome')
# else:
#     print(n,'not a palindrome')   
# n=input('Enter str:')
# vowels='aeiou'
# for i in n:
#     if i in vowels:
#         print(i,end='')
'''print sum of numbers'''
# def sum_num(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum+=digit
#         n=n//10
#     print(sum)
# sum_num(102345)  
# l=[1,2,3,4]
# l1=[l[0]+l[1]+l[2]+l[3]]
# print(l1)      
# l=[1,2,3,4,5]
# l1=sum(l)
# print(l1)
# t=0
# i=1
# while i<=10:
#     t+=i
#     i+=1
# print(t)
# a=0
# for i in range(1,9):
#     a+=i
# print(a)
# l=[1,2,3,4,1,3,2]
# s=set(l)
# print(s)
# l=[1,2,3,4,1,2,5,3]
# e_l=[]
# for i in l:
#     if i not in e_l:
#         e_l.append(i)
# print(e_l)    
# s='ramaaa'
# s1=len(s)
# i=0
# while i<s1:
#     print(s[i])
#     i+=1 
# s='veeresh'
# s1=len(s)-1
# while s1>=0:
#     print(s[s1],end='')
#     s1-=1
# a='veeresh'
# print(a[::-1])