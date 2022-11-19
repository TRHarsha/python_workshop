import os
import time
second = 0
minute = 0
hours =0
stopformat=input("Do you want to stop for second or minute: ")
if stopformat == "second":
    insec=int(input("Enter the seconds"))
    while (second <= insec):
        print("Simple Stopwatch(in Python) ")
        print('\n')
        print(hours, minute, second)
        print('-------------')
        time.sleep(1)
        second += 1
        if (second == 60):
            second = 0
            minute += 1
        if (minute == 60):
            minute = 0
            hours += 1
            os.system('cls')
elif stopformat == "minute":
    inmin=int(input("Enter the minutes: "))
    while (minute <= inmin):
        print("Simple Stopwatch(in Python) ")
        print('\n')
        print(hours, minute, second)
        print('-------------')
        time.sleep(1)
        second += 1
        if (second == 60):
            second = 0
            minute += 1
        if (minute == 60):
            minute = 0
            hours += 1
            os.system('cls')
