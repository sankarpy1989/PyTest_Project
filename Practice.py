import itertools
words = ['fired', 'alert', 'remain', 'alter', 'allergy', 'gallery',
         'abets', 'baste', 'fried', 'beast', 'beats']
anagram_list = []
words1 = sorted(words, key=sorted)
print(words1)
for _, group in itertools.groupby(sorted(words, key=sorted), sorted):
   group = list(group)
   if len(group) > 1:
      anagram_list.append(group)
print(anagram_list)
#
#
# def ischeckprimenumber(num):
#     if num > 1:
#         for i in range(2, int(num/2)+1):
#             if num % i == 0:
#                 print(f"This number {num} is not a prime number")
#                 break
#         else:
#             print(f"This number {num} is a prime number")
#
#     else:
#         print(f"This number {num} is not a prime number")
#

# n = int(input("Enter a number: "))
# ischeckprimenumber(n)

#
# def display_prime_numbers(num1, num2):
#     primenumber_list = []
#     for i in range(num1, num2):
#         if i == 0 or i == 1:
#             continue
#         else:
#             for j in range(2, int(i/2) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 primenumber_list.append(i)
#     return primenumber_list
#
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# result = display_prime_numbers(num1, num2)
# if len(result) == 0:
#     print("There are no prime numbers in this range")
# else:
#     print("The prime numbers in the given range are : ", result)
#
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     return fact
#
# num = int(input("Enter a number: "))
# # Checking if the number is non-negative
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     result = factorial(num)
#     print(f"The factorial of {num} is: {result}")


# import math
#
#
# def factorial(num):
#     return math.factorial(num)
#
#
# n = int(input("Enter a number: "))
# print(factorial(n))


# def find_missing(input_list):
#     sum_of_elements = sum(input_list)
#
#     # There is exactly 1 number missing
#     n = len(input_list) + 1
#     actual_sum = (n * (n + 1)) / 2
#
#     return int(actual_sum - sum_of_elements)
#
#
# list_1 = [1, 5, 6, 3, 4]
#
# print(find_missing(list_1))
#
#
# def check_armstrong(num):
#     n = len(str(num))
#     temp = num
#     sum1 = 0
#     while temp > 0:
#         digit = temp % 10
#         sum1 = sum1 + (digit ** n)
#         temp = temp // 10
#
#     return sum1
#
#
# num = int(input("Enter a number: "))
# armstrong_num = check_armstrong(num)
# if num == armstrong_num:
#     print(f"The number {num} is a Armstrong Number")
# else:
#     print(f"The number {num} is not a Armstrong Number")
#
#
# def LeapYear(year):
#     if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
#         print("This given year is a LeapYear")
#     else:
#         print("This give year is not a leap year")
#
#
# year = int(input("Enter a year: "))
# LeapYear(year)


# fib_num = [0, 1]
# 
# num = int(input("Enter a number: "))
# 
# while fib_num[-1] <= num:
#     fib_num.append(fib_num[-1] + fib_num[-2])
# 
# if num in fib_num:
#     print(f"Yes, {num} is a fibonacci number.")
# else:
#     print(f"Yes, {num} is not a fibonacci number.")

# def len_number(num):
#     if num >= 0:
#         raise ValueError("Please enter a positive integer greater than 0.")
#     count = 0
#     while num > 0:
#         count = count + 1
#         num = num // 10
#     return count
#
# try:
#     num = int(input("Enter a number: "))
#     print(len_number(num))
# except ValueError as e:
#     print(f"Error: {e}")
#
#
# def len_number(num):
#     count = 0
#     while num > 0:
#         count = count + 1
#         num = num // 10
#     return count
#
#
# num = int(input("Enter a number: "))
# print(len_number(num))


# n = [1,4,5,6,7,9]
# print(n[2:16])
#
# print(n[-16])


# a =(1,2)
# a[0] +=1
# print(a)
#
# a = (1,2)
# a +=(-2, -1)
# print(a)
#
# list =[1,2,3,4,5]
# print(list(set([1,1,2,3,4,4])))


# class Test:
#     def __init__(self):
#         self._c = 1
#         self.__c = 2
#         self.__c_ = 3
#         self.__c__ = 4
#
# obj =Test()
# print(obj._c)
# print(obj.__c)
# print(obj.__c_)
# print(obj.__c__)


s = [1, 'p', 2, 3, 'y', 't', 4, 'h']
l1 = []
l2 = []
for i in range(len(s)):
    if type(s[i]) == str:
        l1.append(s[i])
    else:
        l2.append(s[i])

new = []
for i in range(len(l2)):
    new.append((l2[i], l1[i]))
print(new)


def swap_letters(s):
    letters = [char for char in s if char.isalpha()]
    s1 = list(s)
    print(s1)
    for i, char in enumerate(s1):
        if char.isalpha():
            s1[i] = letters.pop(-1)
    return "".join(s1)


s = "ad83hs123mn87ep"
print(swap_letters(s))

def longest_unique_substring(s):
    start = 0
    max_length = 0
    current_start = 0
    char_index_map = {}
    for i in range(len(s)):
        if s[i] in char_index_map and char_index_map[s[i]] >= start:
            start = char_index_map[s[i]] + 1

        char_index_map[s[i]] = i
        current_length = i - start + 1

        if current_length > max_length:
            max_length = current_length
            current_start = start
    return s[current_start: current_start + max_length]


s = "abcabcdebb"
print(longest_unique_substring(s))
