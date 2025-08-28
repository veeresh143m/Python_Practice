                              # Move all zeros to the end of a list (maintaining order)
#
# li = [5,1,3,0,8,18,29,0,19,99,0,87]
# new_list = []
# li.sort()
# for i in li:
#     if i != 0:
#         new_list.append(i)
# for i in li:
#     if i == 0:
#         new_list.append(0)
# print(new_list)

                             # Find the most frequent element in a list.

# li = [5,1,3,1,8,18,29,1,19,99,1,87]
# max_count = 0
# frequent_count = li[0]
# for i in li:
#     count = li.count(i)
#     if count > max_count:
#         max_count = count
#         frequent_count =i
# print(frequent_count)

                                        # Check if two strings are anagrams.
        # meaning: both strings contain the same letters with the same frequency, just in different order.

# str1 = 'listen'
# str2 = 'silent'
# if sorted(str1) == sorted(str2):
#     print('Anagrams')
# else:
#     print('Not Anagrams')


                             # *
                             # * *
                             # * * *
                             # * * * *

# n = 4
# for i in range(1,n+1):
#     print('* ' * i)

                             # Write a function to return all prime numbers in a range.
#
# def prime_number(start,end):
#     for num in range(start,end + 1):
#         count = 0
#         if num > 1:
#             for i in range(2,num):
#                 if num % i == 0:
#                     count += 1
#             if count == 0:
#                 print(num)
# prime_number(1,10)


                             # Check if a number is an Armstrong number.Check if a number is an Armstrong number.
                             
# n = int(input("Enter Number :"))
# sqr = len(str(n))
# num = n
# arm_num = 0
# while n > 0:
#     digit = n % 10
#     arm_num += digit ** sqr
#     n = n // 10
# if arm_num == num:
#     print('Armstrong Number')
# else:
#     print("Not a Armstrong Number")
# s1='cool'
# s2='looc'
# if sorted(s1)==sorted(s2):
#     print(s1,s1)
# else:
#     print('not match')    
# def my_decorator(func):
#     def wrapper(name):
#         print('hello')
#         func(name)
#         print('hello',name,'how are you')
#     return wrapper
# @my_decorator
# def greet(name): 
#     print(name,'your work is finished')
# greet('veeresh')  
# def my_function():
#     yield 1
#     yield 2
#     yield 3
# m=my_function()   
# for v in m:
#     print(v) 
# def my_function(n):
#     i=1
#     while i<=n:
#         yield i
#         i+=1
# for num in my_function(5):
#     print(num)        
# str='veeresh'
# i=0
# s=len(str)
# while i<s:
#     print(str[i])
#     i+=1
# str='veeresh'
# i=len(str)-1
# while i>=0:
#     print(str[i])
#     i-=1


         


      