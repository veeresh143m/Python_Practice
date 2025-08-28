'''for loop
while loop'''
# for i in range(1,20):
#     if i%2!=0:
#         print(i)
# n=int(input('Enter the number:'))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
# i=1
# while i<10:
#     i+=1
#     print(i)
# num=1
# while num<=5:
#     if num%2==0:
#         print(f"{num} is even number")
#     else:
#         print(f"{num} is odd number")  
#     num+=1   
# 
# 
# n=input("Enter the name:")
# l=len(n)
# i=0
# while i<l:
#     print(n[i],end=' ')
#     i+=1   
# n=input('enter the name:')
# for i in n[::-1]:
#     print(i,end='')
# a=input('enter the name:')
# for i in a:
#     print(i)
# def even_odd(user):
#     user=int(input('enter the number')) 
#     if user%2==0:
#         print('even nuber')
#     else:
#         print('odd number')
    
# even_odd()         
# for i in range(1,9):
#     if i==4:
#         print('loop is breaking')
#         break
#     print(i)
# cart=[1,2,100,200,300,220,400]
# for i in cart:
#     if i>=300:
#         print(i)
# a=[1,2,3,4,5]
# for i in a:
#     a.remove(i)
# print(a)   
# a=[1,0,3,0,2,2,0,4,0] 
# for i in a:
#     if i==0:
#         a.remove(i)
#         a.append(i)
#     print(a)
# str='hello veeresh how are you'
# c=str.title()
# print(c)
# a=[1,2,3,4]
# for i in a:
#     print(i+10)
# a=['rama','sita','lava','kusha']
# b=[i[0] for i in a]
# print(b)
# a='veeresh raj kumar'
# v='aeiou'
# for i in a:
#     if i in v:
#         print(i)
# a=int(input('Enter the number:'))
# fact=1
# for i in range(1,a+1):
#     fact*=i
#     print(fact)
# n=int(input('Enter the nuber:'))
# a=0
# b=1
# for i in range(n):
#     a,b=b,b+a
#     print(a)
# a=[1,2,3,4]
# b=[6,7,8]
# a.extend(b)
# print(a)
# a=[1,2,3,4]
# a.insert(3,333)
# print(a)
'''armstrong number'''
# num = int(input("Enter a number: "))

# n = len(str(num))        # Count digits
# sum = 0
# temp = num

# while temp > 0:
#     digit = temp % 10     # Get last digit
#     sum += digit ** n     # Add digit^n
#     temp //= 10           # Remove last digit

# if sum == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")   
num=int(input('Enter the number:'))


       















