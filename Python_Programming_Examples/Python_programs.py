# Write a python program to convert a list of key-value pairs to dictionary
def list_to_dict(li):
    dct = {li[i]: li[i + 1] for i in range(0, len(li), 2)}
    return dct


li = ['a', 1, 'b', 2, 'c', 3, 'd', 4]
print(list_to_dict(li))

# convert two lists into dictionary

# keys = [1, 2, 3, 4]
# values = [5, 6, 7, 8]
# result = dict(zip(keys, values))
# print(result)
#

# lkeys = ["Mon", "Tue", "Wed", "Thu"]
# lvalues = [1, 2, 3, 4]
# result = {lkeys[i]:lvalues[i] for i in range(len(lkeys))}
# print(result)


# Remove duplicate values
# x = [1, 2, 5, 7, 3, 5, 8, 1]
# c = []
# for i in x:
#     if i not in c:
#         c.append(i)
# print(c)

# Remove duplicate values and print remaining values
# x = [1, 2, 5, 7, 3, 5, 8, 1]
# y = []
# for i in x:
#     if x.count(i) == 1:
#         y.append(i)
# print(y)


# Second-highest value in list

# l = [4, 5, 7, 1, 8]
# l.sort()
# print(l[-2])

# count the repeated values
# v = "Regression testing is nothing but a full or partial selection"
# d = {}
# for i in v:
#     d[i] = d.get(i, 0) + 1
# print(d)


# v = "Regression testing is nothing but a full or partial selection"
# l = []
# for i in v:
#     if i not in l:
#         l.append(i)
#
# for i in l:
#     print('{} occurrences {} times'.format(i, v.count(i)))

# s = "ssssfffbbbccc"
# o = ""
# for i in s:
#     if i not in o:
#         o = o + i
# print(o)

# Count the elements in string
# string = "The best of both worlds"
# count = 0
# for i in range(0, len(string)):
#     if (string[i] != " "):
#         count = count + 1
# print("Total number of characters in a string: " + str(count))

# s = input("Enter the string: ")
# total = 0
# for i in s:
#     total += 1
# print(total)



# Merging two lists

# a = [3, 4, 6, 8, 10, 11, 14, 15]
# b = [1, 2, 5, 7, 9, 12, 13, 16, 33, 60]
# c = []
# index_a = 0
# index_b = 0
# while index_a < len(a) and index_b < len(b):
#     if a[index_a] < b[index_b]:
#         c.append(a[index_a])
#         index_a += 1
#     else:
#         c.append(b[index_b])
#         index_b += 1
# if len(a) > len(b):
#     c.extend(a[index_a:len(a)])
# else:
#     c.extend(b[index_b:len(b)])
# print(c)

# Reverse merge two lists
# a = [3, 4, 6, 8, 10, 11, 14, 15]
# b = [1, 2, 5, 7, 9, 12, 13, 16, 33, 60]
# c = []
# index_a = len(a)
# index_b = len(b)
# while index_a > 0 and index_b > 0:
#     if a[index_a-1] < b[index_b-1]:
#         c.append(a[index_a-1])
#         index_a -= 1
#     else:
#         c.append(b[index_b-1])
#         index_b -= 1
# if len(a) > len(b):
#     c.extend(a[(index_a-1)::-1])
# else:
#     c.extend(b[(index_b-1)::-1])
# print(c)

# Write a program 123 --> 321 and -123 > -321

# def rever(x):
#     x = str(x)
#     if x[0] =="-":
#         a = x[::-1]
#         return f"{x[0]}{a[:-1]}"
#     else:
#         return x[::-1]
#
# print(rever("abc"))
# print(rever(123))
# print(rever(-123))


# Write a Python program to check prime numbers.

# def PrimeChecking(num):
#     # Condition to check given number is more than 1
#     if num > 1:
#         # For loop to iterate over the given number
#         for i in range(2, int(num/2) + 1):
#             # Condition to check if the given number is divisible
#             if (num % i) == 0:
#                 #If divisible by any number it's not a prime number
#                 print("The number ",num, "is not a prime number")
#                 break
#         # Else print it as a prime number
#         else:
#             print("The number ",num, "is a prime number")
#     # If the given number is 1
#     else:
#         print("The number ",num, "is not a prime number")
# # Input function to take the number from user
# num = int(input("Enter a number to check prime or not: "))
# # To print the result, whether a given number is prime or not
# PrimeChecking(num)


# Write a Python program to calculate the square root of a given number.

# Input function to get the input from the user
# n = float(input('Enter a number: '))
#
# #Formula to calculate the square root of the number
# n_sqrt = n ** 0.5
#
# #Printing the calculated square root of the given number
# print('The square root of {0} is {1}'.format(n ,n_sqrt))


#  Write a Python program to calculate the area of a triangle.
# Python Program to find the area of a triangle

# Get the 3 sides of a triangle from the user
# s1 = float(input('Enter first side value: '))
# s2 = float(input('Enter second side value:'))
# s3 = float(input('Enter third-side value:'))
#
# #Calculating the semi-perimeter of a triangle
# sp = (s1 + s2 + s3) / 2
#
# #Calculating the area of a triangle
# area = (sp*(sp-s1)*(sp-s2)*(sp-s3)) ** 0.5
#
# #Printing the area of the triangle
# print('The area of the triangle is: ', area)


# Write a Python program to check leap year.

#Python program to check whether the given year is leap year or not

# Function implementation to check leap year
# def LeapYear(Year):
#   #Condition to check if the given year is leap year or not
#   if((Year % 400 == 0) or
#      (Year % 100 != 0) and
#      (Year % 4 == 0)):
#     print("The given Year is a leap year");
#   # Else it is not a leap year
#   else:
#     print ("The given Year is not a leap year")
# # Taking an input year from user
# Year = int(input("Enter the year to check whether a leap year or not: "))
# # Printing the leap year result
# LeapYear(Year)


# Write a Python Program to Find Vowels From a String.

# def get_vowels(String):
#     return [each for each in String if each in "aeiou"]
# get_string1 = "hello" # ['e', 'o']
# get_string2 = "python is fun" # ['o', 'i', 'u']
# get_string3 = "coding compiler" # ['o', 'i', 'o', 'i', 'e']
# get_string4 = "12345xyz" # []


#  Write a Python Program to Count the Number of Vowels in a String?

# string=raw_input("Enter string:")
# vowels=0
# for i in string:
# if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
# vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)
#
#
# #Let's print vowels from the given strigns
# #Vowels from first string
# print("The Vowels Are:  ",get_vowels(get_string1))
#
# #Vowels from second string
# print("The Vowels Are:  ",get_vowels(get_string2))
#
# #Vowels from third string
# print("The Vowels Are:  ",get_vowels(get_string3))
#
# #Vowels from fourth string
# print("The Vowels Are:  ",get_vowels(get_string4))

# def freq_words():
#    str = input("Enter a string: ")
#    l = str.split()
#    d = {}
#
#    for i in l:
#       if i not in d.keys():
#          d[i] = 0
#       d[i] = d[i] + 1
#    print(d)
#
# freq_words()


# def freq_words():
#    str = input("Enter a string: ")
#    l = str.split()
#    d = {}
#
#    for i in l:
#       d[i] = d.get(i, 0) + 1
#    print(d)
#
#
# freq_words()


# Write a Python Program to Check Common Letters in Two Input Strings?

# s1=input("Enter first string:")
# s2=input("Enter second string:")
# a=list(set(s1)&set(s2))
# print("The common letters are:")
# l = []
# for i in a:
#    print(i)

# Write python program to find out the missing number

# def MissingNumber(arr):
#    i, sum1 = 0, 1
#    n = len(arr)
#    for i in range(2, n + 2):
#       sum1 += i
#       sum1 -= arr[i - 2]
#    return sum1
#
#
# arr = {1, 2, 3, 4, 5, 6, 7, 8, 10}
# ans = MissingNumber(arr)
# print(ans)

# Finding missing number in any array

# Summation method

# def get_missing_number(a):
#    n = a[-1]
#    sum1 = 0
#    total = n*(n+1)//2
#    sum1 = sum(a)
#    print(total - sum1)
#
# a = [1, 2, 4, 5, 6, 7]
# get_missing_number(a)
# or
# def getMissingNo(arr, n):
#    total = (n + 1) * (n + 2) // 2
#    sum_of_A = sum(arr)
#    return total - sum_of_A
#
#
# arr = [1, 2, 3, 5]
# N = len(arr)
# print(getMissingNo(arr, N))
#
# # XOR Method
#
# def get_missing_num(a):
#    n = len(a)
#    xor_a = a[0]
#    for index in range(1,n):
#       xor_a = xor_a^a[index]
#    x2 = 0
#    for index in range(1, n+2):
#       x2 = x2^index
#    print(xor_a^x2)
#
# a = [1, 2, 4, 5, 6, 7]
# get_missing_num(a)


#
# def twosum(arr, sum):
#    arr.sort()
#    left = 0
#    right = len(arr) - 1
#    while left <= right:
#       if (arr[left] + arr[right] > sum):
#          right = right - 1
#       elif (arr[left] + arr[right] < sum):
#          left = left + 1
#       elif (arr[left] + arr[right] == sum):
#          print("Value of pair are", arr[left], "&", arr[right])
#          right = right - 1
#          left = left + 1
#
# arr = [5, 4, 3, 7, 8, 9, 19, 11]
# sum = 17
# twosum(arr, sum)


s = "abcdefghijklm"

# 1st Solution
# s1 = s[::-1]
#
# print(s1)

# 2nd Solution
# s1 = reversed(s)
# out = "".join(s1)
# print(out)
"""or"""
# print("".join(reversed(s)))

# 3rd Solution
# n = len(s)
# i = n-1
# while i >= 0:
#     print(s[i], end="")
#     i = i-1

# 4th Solution

# s1 = ""
# for i in s:
#     s1 = i + s1
# print(s1)

# 5th Solution
n = int(input("Enter a number: "))
rev = 0
while n != 0:
    rev = (rev*10) + (n%10)
    n //= 10
print("Reverse number : ", rev)


# s = "automation"
# # atom
#
# uniqchar = []
# for i in s:
#     if i not in uniqchar:
#         uniqchar.append(i)
#
# print(uniqchar)
#
# s1 = ""
# for i in uniqchar:
#     if i == "a" or i == "t" or i == "o" or i == "m":
#         s1 = s1 + i
# print(s1)
#
# data = {"s1": {"Name": "Vijay", "Age": 35, "Sal": 15000},
#         "s2": {"Name": "Jai", "Age": 33, "Sal": 12000},
#         "s3": {"Name": "Shiva", "Age": 29, "Sal": 10000}}
#
# for i in data:
#     if data[i]["Age"] >= 30:
#         print(data[i]["Age"])
#
#
# l = [1, 2, 3, 4, 5, 6, 22, 44, 11, 10]
#
# n = int(input("Enter the number of elements: "))
#
#
# def drop_left(a, n):
#     return a[n:]
#
#
# def drop_right(a, n):
#     return a[:-n]
#
#
# result = drop_left(l, n)
# print(result)
#
# result = drop_right(l, n)
# print(result)

import re

# l = ["Vijay@gmail.com", "Jaya@yahoo.com", "Shiva@outlook.com", "Siri@yahoo.com"]
#
# pattren = re.compile(r"[a-zA-Z.]+@[a-zA-Z]+\.(\w+)")
#
# matches = pattren.finditer(str(l))
# for match in matches:
#     print(match.group())


l = ["Vijay@gmail.com", "Jaya@yahoo.com", "Shiva@outlook.com", "Siri@yahoo.com"]

pattren = re.compile(r"[a-zA-Z.]+@yahoo+\.(\w+)")

matches = pattren.finditer(str(l))
for match in matches:
    print(match.group())


data = [
    {"sshUserName": "admin", "groupName": "vpc", "switchName": "SW_95", "switchDbID": "1020", "ipAddress": "10.1.228.95"},
    {"sshUserName": "admin", "groupName": "vpc", "switchName": "SW_146", "switchDbID": "1070", "ipAddress": "10.1.228.146"},
    {"sshUserName": "admin", "groupName": "Policy", "switchName": "SW_192", "switchDbID": "5480", "ipAddress": "10.1.228.192"}
]

ip_addresses = {}

for item in data:
    ip_address_key = "ipAddress"

    if ip_address_key in item:
        ip_address_value = item[ip_address_key]
        ip_addresses[item["switchName"]] = ip_address_value

print(ip_addresses)


# Check if there is a string in the list which has exactly the same letters as in "word".
# A match is when all the letters that appeared in "word" appear in one of the strings in the list.

word = "hello"
list_of_strings = ["hlelo", "Hi", "Bye"]
for i in list_of_strings:
    if sorted(i) == sorted(word):
        print("word is matched")
    else:
        print("words are not matched")

class IPv4Address:
    def __init__(self, address):
        self.address = address
        self.octets = self.parse_address()

    def parse_address(self):
        octets = self.address.split('.')
        if len(octets) != 4:
            raise ValueError("IPv4 address should contain 4 octets.")
        return list(map(int, octets))

    def is_valid_octet(self, octet):
        return 0 <= octet <= 255

    def is_valid_ipv4(self):
        return all(self.is_valid_octet(octet) for octet in self.octets)

# Sample inputs
addresses = ["192.168.1.1", "10.0.0.256", "172.16.0.1", "invalid_address"]

# Check and print results
for address_str in addresses:
    try:
        ipv4_address = IPv4Address(address_str)
        is_valid = ipv4_address.is_valid_ipv4()
        print(f"{address_str} is {'valid' if is_valid else 'invalid'} IPv4 address.")
    except ValueError as e:
        print(f"{address_str} is invalid: {e}")

s = 'aaaabbbccz'
previous = s[0]
s1 = ""
count = 1
i = 1
while i < len(s):
    if s[i] == previous:
        count += 1
    else:
        s1 = s1 + str(count) + previous
        previous = s[i]
        count = 1
    if i == len(s) - 1:
        s1 = s1 + str(count) + previous
    i = i + 1

print(s1)

s = 'aaaabbbccz'
s1 = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        s1 += str(count) + s[i - 1]
        count = 1

# Add the count and last character for the last group
s1 += str(count) + s[-1]
print(s1)

# s = "Welcome to python tutorial"
#
# print(s[-11:-17:-1])
#
# l = list(s)
# print(l)
#
# print(s[-11:-17:-1])

# def add(*a):
#     count = 0
#     for i in a:
#         count += i
#     return count
#
#
# print(add(1, 2, 4, 5))

# def swap_case(s):
#     string = ""
#     for i in range(len(s)):
#         if s[i].islower():
#             string += s[i].upper()
#         elif s[i].isupper():
#             string += s[i].lower()
#         else:
#             string += s[i]
#     return string
#
#
# st = input("Enter a string: ")
# result = swap_case(st)
# print(result)

#
# def swap_case(s):
#     string = ""
#
#     for i in s:
#         if i.isupper():
#             string += i.lower()
#         elif i.islower():
#             string += i.upper()
#         else:
#             string += i
#     return string
#
#
# st = input("Enter a string: ")
# result = swap_case(st)
# print(result)

# L = [2, 3, 4, 5, 6, 4, 5, 8, 1]
#
#
# def listRotate(L):
#
#
# L = [2, 3, 4, 5, 6, 4, 5, 8, 1]
#
# L.append(L.pop(L.index(2)))
# L.append(L.pop(L.index(3)))
# L.append(L.pop(L.index(4)))
# L.append(L.pop(L.index(5)))
# L.append(L.pop(L.index(6)))
#
#
# print(L)

# L = [2, 3, 4, 5, 6, 4, 5, 8, 1]


# def moveitemsfromrtol(lst):
#     return lst[-3:-1] + lst[-1:] + lst[:-3]
#
#
# print(moveitemsfromrtol(L))

# L = [2, 3, 4, 5, 6, 4, 5, 8, 1]
#
#
# def moveitemsfromltor(lst):
#     return lst[5:] + lst[:0] + lst[:5]
#
#
# print(moveitemsfromltor(L))

L = [2, 3, 4, 5, 6, 4, 5, 8, 1]


def moveitemsfromltor(lst):
    print(lst[-3:-1] + lst[-1:] + lst[:-3])
    print(lst[5:] + lst[:0] + lst[:5])


moveitemsfromltor(L)


from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

# Sort the list of dictionaries based on the 'date' key
sorted_rows = sorted(rows, key=lambda x: x['date'])

# Group the sorted rows by date
grouped_rows = {key: list(group) for key, group in groupby(sorted_rows, key=lambda x: x['date'])}

# Print the grouped result with a specific format
for date, addresses in grouped_rows.items():
    print(date)
    for address in addresses:
        print(f"   {address}")

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

# Sort the list of dictionaries based on the 'date' key
sorted_rows = sorted(rows, key=lambda x: x['date'], reverse=True)

# Print the sorted result
for row in sorted_rows:
    print(row)


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

input_string = "abcabcbb"
result = longest_unique_substring(input_string)
print(f"The longest continuous substring with unique elements is: {result}")


def find_missing_number(arr):
    n = len(arr) + 1  # Length of the original array + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)

    missing_number = expected_sum - actual_sum

    return missing_number if missing_number != 0 else None

# Test cases
A1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
missing_number1 = find_missing_number(A1)
print(f"Missing number for A1: {missing_number1}")

A2 = [10, 11, 12, 13, 14, 15, 16, 18, 19, 20]
missing_number2 = find_missing_number(A2)
print(f"Missing number for A2: {missing_number2}")

A3 = [1, 2, 3, 4, 5, 6]
missing_number3 = find_missing_number(A3)
print(f"Missing number for A3: {missing_number3}")

A4 = [-1, 1]
missing_number4 = find_missing_number(A4)
print(f"Missing number for A4: {missing_number4}")


a = ["a", 10, 10, "bcd", 10, "ef"]

strings_list = [str(element) for element in a if isinstance(element, str)]
ints_list = [str(element) for element in a if isinstance(element, int)]

concatenated_strings = ''.join(strings_list)
concatenated_ints = ''.join(ints_list)

print("Concatenated strings:", concatenated_strings)
print("Concatenated ints:", concatenated_ints)


def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

print(sum([5,7,3,8,10]))


l = [1, 2, 3, 4, 6, 7]


def addition(n):
    if len(n) > 1:
        return n[0] + addition(n[1:])
    elif len(n) == 1:
        return n[0]
    else:
        return 0


print(addition(l))

l = [1, 2, 3, 4, 6, 7]


def perform_operation(n, operation='+'):
    if len(n) > 0:
        if operation == '+':
            return n[0] + perform_operation(n[1:], operation)
        elif operation == '-':
            return n[0] - perform_operation(n[1:], operation)
    elif len(n) == 1:
        return n[0]
    else:
        return 0


print(perform_operation(l, '+'))  # Addition: 23
print(perform_operation(l, '-'))  # Subtraction: -21


def sumOfNumbers(N):
    if N == 1:
        return N
    else:
        return N + sumOfNumbers(N - 1)


input_number = 10
output = sumOfNumbers(input_number)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


def power_of_num(num, topwr):
    if topwr == 0:
        return 1
    else:
        return num * power_of_num(num, topwr - 1)


print('{} to the power of {} is: {} '.format(4, 7, power_of_num(3, 7)))
print('{} to the power of {} is: {} '.format(2, 8, power_of_num(4, 3)))


def sumDigits(no):
    if no == 0:
        return 0
    else :
        return int(no % 10) + sumDigits(int(no / 10))
nums = int(input("Enter a number: "))
print("The sum is:", sumDigits(nums))



