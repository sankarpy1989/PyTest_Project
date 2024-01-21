# l = ["a", 1, "b", 2, "c", 3]
# dic = {l[i]:l[i+1] for i in range(0, len(l), 2)}
# print(dic)
#

# Factorial examples
# def factorial(n):
#     if n < 1:
#         return 1
#     else:
#         n = n*factorial(n-1)
#     return n
#
# n= int(input("Enter a number: "))
# print(factorial(n))

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
#
# print(fact)
#

# Fibonacci Examples
# n = int(input("Enter a number: "))
# x = 0
# y = 1
# for i in range(n):
#     print(x, end=",")
#     x, y = y, x+y
#

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# n = int(input("Enter a number: "))
# for i in range(n):
#     print(fibonacci(i))


# Palindrome Examples
# n = input("Enter a string: ")
# if n == n[::-1]:
#     print(f"{n} is a palindrome")
# else:
#     print(f"{n} is not a palindrome")
#
#
# n = int(input("Enter a number: "))
# def palindrome(n):
#     temp = n
#     res = 0
#     while temp > 0:
#         digit = temp % 10
#         res = res * 10 + digit
#         temp = temp // 10
#     if res == n:
#         print(f"{n} number is a palindrome")
#     else:
#         print(f"{n} number is not a palindrome")
#
# palindrome(n)
#
#
# def palindrome(s):
#     if len(s) > 1:
#         return True
#     else:
#         if s[0] != s[-1]:
#             return False
#         else:
#             return palindrome(s[1:-1])
#
#
# s = input("Enter a string: ")
# if palindrome(s):
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")

# def find_longest_palindrome(s):
#     longest = ""
#     n = len(s)
#     for i in range(n):
#         for j in range(i+1, n+1):
#             word = s[i:j]
#             if word == word[::-1]:
#                 if len(word) > len(longest):
#                     longest = word
#     return longest
#
# s = input("Enter a string: ")
# print(find_longest_palindrome(s))


# Armstrong Number Examples
# def armstrong(num):
#     n = len(str(num))
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum = sum + digit ** n
#         temp = temp // 10
#     if sum == num:
#         print(f"{num} is a Armstrong number")
#     else:
#         print(f"{num} is not a Armstrong Number")
#
# num = int(input("Enter a number: "))
# armstrong(num)
#
#
# def armstrong(num):
#     n = len(str(num))
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum = sum + digit ** n
#         temp = temp // 10
#     return sum == num
#
#
# lower = int(input("Enter a lower level number: "))
# upper = int(input("Enter a upper level number: "))
#
# for i in range(lower, upper):
#     if armstrong(i):
#         print(i)


# Missing Number Example

# def missing_number(arr):
#     i, sum = 0, 1
#     n = len(arr)
#     for i in range(2, n + 2):
#         sum = sum + i
#         sum = sum - arr[i - 2]
#     return sum
#
#
# arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
# print(missing_number(arr))

# def find_missing_number(arr):
#     n = len(arr) + 1  # Length of the original array + 1
#     expected_sum = (n * (n + 1)) // 2
#     actual_sum = sum(arr)
#
#     missing_number = expected_sum - actual_sum
#
#     return missing_number if missing_number != 0 else None
#
#
# # Test cases
# A1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# missing_number1 = find_missing_number(A1)
# print(f"Missing number for A1: {missing_number1}")

# def freq_words():
#     s = input("Enter a string: ")
#     l = s.split()
#     d = {}
#     for i in l:
#         d[i] = d.get(i, 0) + 1
#     return d
#
#
# print(freq_words())
#
#
# s = "Python Tutorial class"
# d = {}
# for i in s:
#     d[i] = d.get(i, 0) + 1
# print(d)
#
#
# s = "Python programming language"
# l = []
# for i in s:
#     if i not in l:
#         l.append(i)
#
#
# for i in l:
#     print("{} occurrences {} times".format(i, s.count(i)))

#
# s = "ssssfffbbbccc"
# o = ""
# for i in s:
#     if i not in o:
#         o = o + i
# print(o)
#
# # Count the elements in string
# string = "The best of both worlds"
# count = 0
# for i in range(0, len(string)):
#     if string[i] != " ":
#         count = count + 1
# print("Total number of characters in a string: " + str(count))
#
#
# s = 'aaaabbbccz'
# previous = s[0]
# s1 = ""
# count = 1
# i = 1
# while i < len(s):
#     if s[i] == previous:
#         count += 1
#     else:
#         s1 = s1 + str(count) + previous
#         previous = s[i]
#         count = 1
#     if i == len(s)-1:
#         s1 = s1 + str(count) + previous
#     i = i + 1
#
# print(s1)

# l = [1, 10, 5, 6, 3, 4, 11, 43, 23, 44, 87, 9]
# for i in range(len(l)-1):
#     for j in range(len(l)-1):
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
#
# print(l)

# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
#
# print(l)


#
#
# l = [1, 10, 5, 6, 3, 4, 11, 43, 23, 44, 87, 9]
#
# for i in range(0, len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] >= l[j]:
#             l[i], l[j] = l[j], l[i]
#
# print(l)

#
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


def convertToBinary(n):
    if n > 1:
        convertToBinary(n // 2)
    print(n % 2, end="")

dec = 34

convertToBinary(dec)
print()


def decimalToBinary(n):
    return bin(n).replace("0b", "")


print(decimalToBinary(78))


def decimalToBinary(n):
    return "{0:b}".format(int(n))


print(decimalToBinary(36))


def binaryToDecimal(n):
    return int(n, 2)


print(binaryToDecimal('100'))

# Find the max value in the below two lists

list1 = [3, 8, 12, 5]
list2 = [10, 4, 6, 15]

max_value = float('-inf')  # Initialize with negative infinity to ensure any value in the lists will be greater

for val1, val2 in zip(list1, list2):
    if val1 > max_value:
        max_value = val1
    if val2 > max_value:
        max_value = val2

print("Maximum value:", max_value)

str1 = """eth0      Link encap:Ethernet  HWaddr 08:00:27:fd:1f:04              
inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0  
inet6 addr: fe80::a00:27ff:fefd:1f04/64 Scope:Link         
UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1         
RX packets:11894 errors:0 dropped:0 overruns:0 frame:0     
TX packets:8887 errors:0 dropped:0 overruns:0 carrier:0    
collisions:0 txqueuelen:1000                               
RX bytes:2523362 (2.5 MB)  TX bytes:790877 (790.8 KB)"""

import re

# Use regular expression to find the HWaddr
hwaddr_match = re.search(r"HWaddr\s+([0-9a-fA-F:]+)", str1)

if hwaddr_match:
    hwaddr = hwaddr_match.group(1)
    print("HWaddr:", hwaddr)
else:
    print("HWaddr not found in the provided information.")


data = """eth0      Link encap:Ethernet  HWaddr 08:00:27:fd:1f:04              
inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0  
inet6 addr: fe80::a00:27ff:fefd:1f04/64 Scope:Link         
UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1         
RX packets:11894 errors:0 dropped:0 overruns:0 frame:0     
TX packets:8887 errors:0 dropped:0 overruns:0 carrier:0    
collisions:0 txqueuelen:1000                               
RX bytes:2523362 (2.5 MB)  TX bytes:790877 (790.8 KB)"""

# Extract IP address
ip_match = re.search(r'inet addr:(\d+\.\d+\.\d+\.\d+)', data)
if ip_match:
    ip_address = ip_match.group(1)
    print(f"IP Address: {ip_address}")

# Extract hardware address
hwaddr_match = re.search(r'HWaddr ([\da-fA-F:]+)', data)
if hwaddr_match:
    hw_address = hwaddr_match.group(1)
    print(f"Hardware Address: {hw_address}")


def extract_ip_and_hwaddr(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

        # Extract IP address
        ip_match = re.search(r'inet addr:(\d+\.\d+\.\d+\.\d+)', data)
        if ip_match:
            ip_address = ip_match.group(1)
            print(f"IP Address: {ip_address}")

        # Extract hardware address
        hwaddr_match = re.search(r'HWaddr ([\da-fA-F:]+)', data)
        if hwaddr_match:
            hw_address = hwaddr_match.group(1)
            print(f"Hardware Address: {hw_address}")

# Replace 'your_file.txt' with the path to your actual text file
file_path = 'your_file.txt'
extract_ip_and_hwaddr(file_path)
