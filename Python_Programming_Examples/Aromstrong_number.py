# Armstrong number

# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit **3
#     temp //= 10
# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")


# Q1) Write a Python program to check whether the given number is Armstrong or not.

num = int(input("Enter a number: \n"))

# count digits in 'num'
n = len(str(num))

temp = num
sumNum = 0

# calculate sum of digits raised to the power 'n'
while temp > 0:
    sumNum = sumNum + (temp % 10) ** n
    temp = temp // 10

# check if sum equals the original number
if sumNum == num:
    print("Armstrong Number \n")
else:
    print("Not an Armstrong Number \n")


# Q2) To find all Armstrong numbers in the given interval

def isArmstrong(num):
    # count digits in 'num'
    n = len(str(num))

    temp = num
    sumNum = 0

    # calculate sum of digits raised to the power 'n'
    while temp > 0:
        sumNum = sumNum + (temp % 10) ** n
        temp = temp // 10

    # check if sum equals the original number
    return sumNum == num


lower = int(input("Enter lower interval value: "))
upper = int(input("Enter upper interval value: "))

for i in range(lower, upper):
    if isArmstrong(i):
        print(i)



