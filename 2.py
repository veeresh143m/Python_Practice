# n=int(input('Enther the nuber:'))
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print(fact,end=' ')
# n=int(input('Enther the nuber:'))
# fact=1
# value=1
# while fact<n:
#     value*=fact
#     print(value)
#     fact+=1
# num=int(input('Enther the nuber:'))
# n=len(str(num))
# temp=num
# sum=0
# for i in range(n):
#     digit=temp%10
#     sum+=digit**n
#     temp//=10
# if sum==num:
#     print(sum,'this is armstrong number')
# else:
#     print(sum,'this not a armstrong number')    
# num=int(input('Enther the nuber:'))
# n=len(str(num))
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit**n
#     temp//=10
# if sum==num:
#     print(sum)
# else:
#     print('not match')   
# n=int(input('Enther the nuber:'))  
# a=0
# b=1
# for i in range(n):
#     print(a)
#     a,b=b,a+b  
# n=int(input('Enther the nuber:'))
# a=0
# b=1
# count=1
# while count<n:
#     print(a)
#     a,b=b,b+a
#     count+=1
# n=int(input('Enther the nuber:'))
# num=int(str(n)[::-1])
# if num==n:
#     print(num,'is palindrom number')
# else:
#     print(num,'is not a palindrom')
# def palindrom(s):
#     res=''
#     for i in s:
#         res=i+res
#     if res==s:
#         print(res,'this is palindrom str')
#     else:
#         print(res,'this is not a palindrome string')
# palindrom('aba')     
# l1=[1,2,3,4] 
# l2=['ram','sita',20,30] 
# l3=dict(zip(l1,l2))  
# print(l3)     
# nums = [10, 20, 4, 45, 99, 99]
# unique_nums = list(set(nums))   # Remove duplicates
# unique_nums.sort()
# print("Second largest:", unique_nums[-2])
# num = 13  # You can change this value

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is NOT a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is NOT a prime number")
# n=int(input('Enter the number:'))
# if n>1:
#     for i in range(2,n):
#         if i%2==0:
#             print(i,'is a prime number')
#         else:
#             print(i,'is not  a prime')  
  
# name='veeresh is best player'
# s=name.split()
# s1=len(s)-1
# l=[]
# while s1>=0:
#     l.append(s[s1])
#     s1-=1
# print(' '.join(l))   

# name=input('Enter the st:')
# s=name.split()
# s1=len(s)
# l=[]
# i=0
# while i<s1:
#     l.append(s[i][::-1])
#     i+=1
# print(' '.join(l))       
# s=input('Enter the str:')
# i=0
# v='aeiou'
# for p in s:
#     if p in v:
#       print(p[i])
# s=input('Enter the str:')
# count=0
# v='aeiou'
# for s1 in s:
#     if s1 in v:
#         count+=1
# print(count)
# a=[1,1,2,3,4,5,4,6,7,8,9]
# l=[]
# for i in a:
#     if i not in l:
#         l.append(i)
# print(l)        
# l=[1,2,3,4,5]
# t=0
# for i in l:
#     t+=i
# print(t)




