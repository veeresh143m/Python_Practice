'''fibonacci number'''
# n=int(input('Enter the number:'))
# a,b=0,1
# for i in range(n):
#     print(a,end=' ') 
#     a,b=b,b+a 
# n=int(input('Enter the number:'))
# a,b=0,1
# count=1
# while count<n:
#     print(a,end=' ')
#     a,b=b,b+a
#     count+=1
'''armstrong number'''
# num=int(input('Enter the number:'))
# n=len(str(num))
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit**n
#     temp//=10
# if sum==num:
#     print(num,'armstrong number')
# else:
#     print(num,'not a armstrong number')  
'''factorial number''' 
# n=int(input('Enter the number:'))
# fact=1
# for i in range(1,n):
#     fact*=i
#     print(fact,end=' ')   
# n=int(input('Enter the number:'))
# fact=1
# value=1
# while value<n:
#     fact*=value
#     print(fact,end=' ')
#     value+=1 
'''palindrom number'''
# n=int(input('Enter the number:'))
# rev=int(str(n)[::-1])
# if rev==n:
#     print(rev,'is a palindrome number')
# else:
#     print(rev,'not a palindrome')    
'''palindrome string'''
# def palindrome(s):
#     rev=''
#     for i in s:
#         rev=rev+i
#     if rev==s:
#         print(rev) 
#     else:
#         print('not match')
# palindrome('aba') f palindrome(s):
# n=input('enter str:')
# r=''
# for i in n:
#     r=r+i
# if r==n:
#         print(r)
# else:
#         print('not match')    
'''even or odd'''
# n=int(input('Enter the number:'))
# for i in range(n):
#     if i%2==0:
#         print(i,'even')
#     else:
#         print(i,'odd') 
'''string'''
# s='veeresh' 
# for i in range(len(s)):
#     print(s[i],end=' ')  
# s='veeresh'
# i=0
# while i<len(s):
#     print(s[i],end=' ')
#     i+=1   
'''reverse string'''
# s='veeresh' 
# for i in range(len(s)-1,-1,-1):  
#     print(s[i],end=' ') 
# s='veeresh'
# i=len(s)-1
# while i>=0:
#     print(s[i],end=' ')
#     i-=1    
'''string words reverse'''
# n=input('Enter the str:')
# s=n.split()
# l1=[]
# s1=len(s)-1
# i=0
# while s1>=0:         or 0<=s1
#     l1.append(s[s1])
#     s1-=1
# print(' '.join(l1)) 
'''print vowels'''
# n=input('NEter the str:')
# v='aeiou'
# for i in n:
#     if i in v:
#         print(i,end=' ')
'''print how many voewsl in given string'''
# n=input('Enter the str:')
# count=0
# v='aeiou'
# for i in n:
#     if i in v:
#         count+=1
# print(count)    
'''remove duplicates in list'''
# l=[1,2,3,4,2,3,5,6,7,2]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
# l=[1,4,7,8,0,3,6,2,5,4,4,1]
# l1=[]
# i=0
# while i<len(l):
#     l1.append(i)
#     i+=1
# print(l1)
'''print two lists common elements'''
# l1=[1,2,3,4,5]
# l2=[3,4,5,6,7]
# for i in l1:
#     if i in l2:
#         print(i,end=' ')
'''sum of all list elements'''
# l=[1,2,3,4,5,6,7]
# t=0
# for i in l:
#     t+=i
# print(t)
'''print a vowel how many times repeated in the string'''
# def count_v(str,char):
#     vowels='aeiou'
#     count=0
#     for i in str:
#         if i==char:
#             count+=1
#     print(f'the name is {str}, and the character is {char} ,{count} times repeated')
# count_v('veeresh kumar','e')  
''' sort a list without using sort function'''  
# l=[2,5,6,34,4,8,9]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[j]>l[i]:
#           l[i],l[j]=l[j],l[i]
# print(l) 
# l=[2,5,6,34,4,8,9]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#           l[i],l[j]=l[j],l[i]
# print(l)  
'''print a table in reverse'''
# n=int(input('Enter the number:'))
# for i in range(n,0,-1):
#     print(i,'*',n,'=',i*n)
'''enumerate() function'''
# l=['sai','sir','ram','hari']
# for k,v in enumerate(l):
#     print(k,v)
'''zip() fuction'''
# l1=[1,2,3,4]
# l2=[3,4,5,6]
# l3=zip(l1,l2)
# print(list(l3))
# d1=('sai','ram','raj','tej')
# d2=(10,20,30,40)
# print(dict(zip(d1,d2)))
'''print the prime numbers'''
# for i in range(1,20):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)   
'''another''' 
# for i in range(1,20):
#     count=0
#     if i>0:
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i)        
'''find the second largest number'''
# l=[1,20,30,50,80]
# l1=list(set(l))
# l1.sort()
# print(l1[-2])
'''find missing a number in list'''
# l=[1,2,3,4,6]
# n=len(l)+1
# print(n*(n+1)//2-sum(l))

# l=[1,2,3,4,7]
# l1=len(l)+2
# print(l1*(l1+1)//2-sum(l))
'''print how many times appears in a number in list'''
'''first way'''
# l=[1,2,2,3,3,4,4,4,4]
# d={}
# for l1 in l:
#     d[l1]=d.get(l1,0)+1
# print(d)
'''second way'''
# l=[1,1,2,3,3,3,4,4]
# count={}
# for l1 in l:
#     if l1 in count:
#         count[l1]+=1
#     else:
#         count[l1]=1
# for k,v in count.items():
#     print(k,v)            

                         





                       
                     




              


