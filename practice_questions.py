# Reverse a string without using reversed() or [::-1]
#
# Check if a number is even or odd.
#
# Swap two variables without using a third variable.
#
# Print the Fibonacci series up to N terms.
#
# Check if a string is a palindrome.
#
# Count vowels in a string.
#
# Sum of digits of a number.
#
# Find the factorial of a number using recursion.
#
# Remove duplicates from a list.
#
# Find the maximum and minimum number in a list.
#
# Medium Python Coding Questions
#

                             # Reverse a string without using reversed() or [::-1]
# s = 'python'
# res = ''.join (reversed(s))
# print(res)

# s = 'python'
# res = s[::-1]
# print(res)

                             #Check if a number is even or odd.
# n = 10
# if n % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")
#


                             #Swap two variables without using a third variable.
# a = 10
# b = 20
# a,b = b,a
# print(a,b)


                             #Print the Fibonacci series up to N terms
# def fabonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a , b = b , a + b
#     print(a)
# fabonacci(10)


                             #Check if a string is a palindrome.
# def palindrome(s):
#     res = ''
#     for i in s:
#         res = i + res
#     if res == s:
#         print("It is a Palindrome")
#     else:
#         print("It is  not a Palindrome")
# palindrome('aba')


                             #Count vowels in a string
# def count_vowels(s):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for i in s:
#         if i in  vowels:
#             count += 1
#     print(count)
# count_vowels('abioahd')


                             #Sum of digits of a number.
# def sum_digits(n):
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit
#         n = n // 10
#     print(sum)
# sum_digits(7702901916)
# def sum_digits(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum+=digit
#         n=n//10
#     print(sum)
# sum_digits(20304455)        


                             #Find the factorial of a number using recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(10))


                             # Remove duplicates from a list.
# def remove_duplicate(s):
#     no_duplicate = []
#     for i in s:
#         if i not in no_duplicate:
#             no_duplicate.append(i)
#     print(no_duplicate)
# user = input("Enter Number Separated By Space :")
# s = list(map(int,user.split()))
# remove_duplicate(s)


                             # Find the maximum and minimum number in a list.
# def max_min_num(li):
#     max = li[0]
#     for i in li:
#         if i > max:
#             max = i
#     print(max)
#
#     min = li[0]
#     for i in li:
#         if i < min:
#             min = i
#     print(min)
#
# max_min_num([1,88,9,55,4,885])


                             # Find the length of a string without using len().
# def length_of_string(s):
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
#
# length_of_string('python')



                             # Count how many times a given character appears in a string.
# def count_of_char(str,char):
#     count = 0
#     for i in str:
#         if i == char:
#             count += 1
#     print(f'In a given {str} the {char} should be repeated in {count} times')
# count_of_char('satyanarayana tilak','a')

                             # Second largest number in given list
# li = [1, 8, 5, 88, 56]
#
# max1 = li[0]
# for i in li:
#     if i > max1:
#         max1 = i
#
# max2 = None
# for i in li:
#     if i != max1:
#         if max2 is None or i > max2:
#             max2 = i
# print("Second largest number is:", max2)
'''to print leap year
hence leap year it is divisible by 4 and, not divisible by 100.and 400 als0 divisible'''
# n=int(input('Enter the number:'))
# if (n%4==0 and n%100!=0) or (n%400==0):
#   print(n,'is a leap year')
# else:
#     print(n,'is not a leap year')   
# start=int(input('Enter the year:'))
# end=int(input('ENter the year'))
# for i in range(start,end+1):
#     if (i%4==0 and i%100!=0) or (i%400==0):
#         print(i,'is leap year') 
#     else:
#         print(i,'is not a leap year')  
'''enumarate'''
# fruits=['apple','banana','mango'] 
# for index,value in enumerate(fruits): 
#     print(index,value)
''''''''''''
''''''''''''
''''''
''''''
''''''

# str=input('Enter the str:')
# i=0
# v='aeiou'
# for s in str:
#     if s in v:
#         print(s[i])
   
# a=input('Enter the number:')
# rev='' 
# for i in a:
#     rev=i+rev
# if rev==a:
#     print(rev,'this is palindrome')
# else:
#     print('not a palindrome')   
# def count_str(str,chr):
#     count=0
#     for i in str:
#         if i==chr:
#             count+=1
#     print(f'your {str} string is {chr} repeated to {count} times')
# count_str('veeresh','v')     
# def count_str(str,chr):
#     count=0
#     for i in str:
#         if i==chr:
#             count+=1
#     print(f"the name is {str}, the character is {chr} ,{count} time repeated")
# count_str('veeresh','e')    
# l=[1,2,3,1,2,4,5,6]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
# n=int(input('number:'))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     a,b=b,b+a
# year=int(input('Enter the number:'))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year,'is leap year')
# else:
#     print(year,'is not leap year')  
# start=int(input('Enter the number:'))
# end=int(input('Enter the number:'))
# for i in range(start,end+1):
#     if (i%4==0 and i%100!=0) or (i%400==0):
#         print(f'{i} is a leap year')
#     else:
#         print(f'{i} is not leap year')    


        
            

  

