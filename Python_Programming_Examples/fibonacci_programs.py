# Write a program for fibonacci series
# n = int(input("Enter the number: "))
# x = 0
# y = 1
# for i in range(n):
#     print(x)
#     x,y=y,x+y

# n = int(input("Enter the number: "))
# x = 0
# y = 1
# print(x, y, end = " ")
# for i in range(2, n):
#     z = x + y
#     print(z, end = " ")
#     x = y
#     y = z


# Write a program for fibonacci series using recursive function
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibonacci(n-1)+fibonacci(n-2))
# n = int(input("Enter the number: "))
# print("Fibonacci sequence using recursive: ")
# for i in range(n):
#     print(fibonacci(i))

# Skip the fibonacci series expected output[0,1,1,3,8,13]?
n = int(input("Enter the numbers: "))

x = 0
y = 1
for i in range(n):
    if x != 5 and x != 2:
        print(x)
        x, y = y, x + y
    else:
        x, y = y, x + y


