import math
#Factorial of a number
print("Factorial of a number")
number=int(input("Enter the number: "))
print("Factorial of the number ",number," is ",math.factorial(number))
#Sum of the given numbers
print("\nSum of the given number")
num = int(input("Enter the total number do you want to enter : "))
sum = 0
for i in range(num):
    a = int(input("Enter the number : "))
    sum = sum + a
    average = sum/num
print("Sum of the given numbers",sum)
#Average of the given numbers
print("\nAverage of the given number")
print("Average of the given numbers",average)
# To print Even Numbers in given range
print("\nEven numbers of the given number range")
start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
for num in range(start, end):
    if num % 2 == 0:
        print(num)
# To print odd Numbers in given range
print("\nOdd numbers of the given number range")
start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num)
