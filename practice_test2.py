'''fibonacci umber'''
# def fibo(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a)
#         a,b=b,b+a
# n=int(input('Enter the number:'))
# fibo(n) 
# n=int(input('Enter the numebr:'))
# count=0
# a=0
# b=1
# while count<n:
#     print(a)
#     a,b=b,b+a
#     count+=1
'''armstrong number'''
# num=int(input('Enetr the number:'))
# n=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**n
#     temp//=10
# if sum==num:
#     print(num,'is armstrong')
# else:
#     print('not match')    
'''factorial number'''
# n=int(input('Enter the number:'))
# fact=1
# for i in range(1,n):
#     fact*=i
#     print(fact,end=' ')
# n=int(input('Enter the number:'))
# fact=1
# count=1
# while fact<=n:
#     count*=fact
#     print(count)
#     fact+=1
'''palindrome number'''
# n=int(input('Enter the numebr:'))
# p=int(str(n)[::-1])
# if n==p:
#     print(n)
# else:
#     print('not match')   
'''palindrome string'''
# def palindrome(n):
#     res=''
#     for i in n:
#         res=i+res
#     if res==n:
#         print(res,'is p')
#     else:
#         print('not mactch')
# n=input('Enetr the string')
# palindrome(n)     
'''even or odd'''
# n=int(input('Enetr the nuber:'))
# for i in range(n):
#     if i%2==0:
#         print(i,'is even')
#     else:
#         print(i,'is odd')                      
'''print a string '''
# s='veeresh'
# i=0
# for i in range(len(s)):
#     print(s[i],end=' ')
# s='rahulravichandran'
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1
'''print a reverse string'''
# s='veeresh'
# i=0
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end='')
# s='veeresh'
# i=len(s)-1
# while i>=0:
#     print(s[i],end='')
#     i-=1
'''print a string in reverse order  of  words'''
# s='veeresh is the best employee' 
# a=s.split()
# l=len(a)-1
# list=[]
# while l>=0:
#     list.append(a[l])
#     l-=1
# print(' '.join(list))       
'''print internally content reverse in string'''
# n=input('Enter the string:')
# l=n.split()
# i=0
# l1=[]
# while i<len(l):
#     l1.append(l[i][::-1])
#     i+=1
# print(' '.join(l1)) 
'''count how many vowels in string'''   
# n=input('Enter the string:')
# v='aeiou'
# i=0
# for n1 in n:
#     if n1 in v:
#         i+=1
# print(i) 
# l=[1,2,3,2,3,4,5,6]
# l1=[]
# a=0
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)  
# l1=[1,2,3,4]
# l2=[3,4,5,6]
# for i in l1:
#     if i in l2:
#         print(i)
# l=[1,2,3,4,5,6]
# i=0
# for l1 in l:
#     i+=l1
# print(i)
# l=[1,0,2,0,3,0,4]
# for i in l:
#     if i==0:
#         l.remove(i)
#         l.append(i)
# print(l)
# l=[1,2,3,4,5]
# for l[-1] in l:
#     print(l)
# l=[1,2,3,4,5]
# for a in l:
#     l.remove(a)
# print(l)
# s=input('ENter the string:')
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i-=1
# print(' '.join(l1))   
# s=input('ENter the string:')
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i][::-1])
#     i-=1
# print(' '.join(l1)) 
# s=input('Enter the string:')
# l1=s.split()
# l=[]
# for i in l1:
#     l.append(i[::-1])
# print(' '.join(l))    
        
       

           