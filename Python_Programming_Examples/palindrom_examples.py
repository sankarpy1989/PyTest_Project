# Write a python program to check the below string is palindrome or not
# def palindrome(s):
#     n = len(s)
#     for i in range(n):
#         if s[i] != s[n-i-1]:
#             return False
#         return True
#
# s = "abcdcba"
# print(palindrome(s))

# OR

# string = input("Enter a number: ")
# if (string == string[::-1]):
#     print(f"{string} is palindrome number")
# else:
#     print(f"{string} is not a palindrome number")


def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")



# Write a palindrome program using recursive function
# def check_palindrome(v):
#     if len(v) < 1:
#         return True
#     else:
#         if v[0] == v[-1]:
#             return check_palindrome(v[1:-1])
#         else:
#             return False
#
# var = input("Enter a value: ")
# if (check_palindrome(var)):
#     print("The input is palindrome")
# else:
#     print("The input is not palindrome")


# Write a python program to check the below number is palindrome or not
def palindrome(s):
    temp = s
    rev_s = 0
    while (temp > 0):
        digit = temp % 10
        rev_s = rev_s * 10 + digit
        temp = temp // 10
    if s == rev_s:
        return True
    else:
        return False


num=int(input("Enter a number:"))
print(palindrome(num))


# Write a python program to find longest palindrome in the given string
def find_longest_palindrome(s):
    longest = ''
    n = len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            word = s[i:j]
            if word == word[::-1]:
                if len(word)>len(longest):
                    longest = word
    return longest


s = "abcaacbaxyx"

print(find_longest_palindrome(s))