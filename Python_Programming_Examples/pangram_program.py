
# Write a Python program to check if given string is pangram
def pangram_check(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in str.lower():
            return False

    return True


str = 'The quick brown fox jumps over the lazy dog'
if (pangram_check(str) == True):
    print("Yes")
else:
    print("No")

def pangram_check(input_str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in input_str.lower():
            return False
    return True

strings = ['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs']

for s in strings:
    if pangram_check(s):
        print(f'"{s}" is a pangram')
    else:
        print(f'"{s}" is not a pangram')


# Second solution

# import string
#
# alphabet = set(string.ascii_lowercase)
#
#
# def pangram_check(str):
#     return not set(alphabet) - set(str)
#
# str = 'Pack my box with five dozen liquor jugs'
# if (pangram_check(str.lower()) == True):
#     print("Yes")
# else:
#     print("No")