import math
print("AC  | ( | ) | CE |")
print("------------------")
print("Pi  | e |phi|tau |")
print("------------------")
print("Inv |sin|cos|tan |")
print("------------------")
print("log |ln | ! |RtoD|")
print("------------------")
print("root|sq.|cu.| ^  |")
print("------------------")
print(" /  | - | + | *  |")
print("------------------")
print("rnd | . |exp|gcd |")
print("------------------")
print("  ans   |    =   |")
print("------------------")
operation= input("Enter the operation you want to perform: ")
sym=operation
trignometry=["sin","cos","tan"]
logarithm=["log","ln","RtoD"]
raised=["root","sq.","cu.","^"]
extras=["/","-","+","*","rnd","exp","gcd"]
if operation in trignometry:
    valuen=int(input("Enter the number: "))
    x=math.radians(valuen)
    if sym == "sin":
        sin = math.sin(x)
        print("sin of ",x," is ",sin)
    elif sym == "cos":
        cos = math.cos(x)
        print("cos of ",x," is ",cos)
    else:
        tan = math.tan(x)
        print("tan of ",x," is ",tan)
elif operation in logarithm:
    valuen=int(input("Enter the number: "))
    if sym == "log":
        print("Log of ",valuen," is ",math.log10(valuen))
    elif sym == "ln":
        base=input("Enter the base of ",valuen," : ")
        print("Log of ",valuen," is ",math.log(valuen,basee))
    elif sym == "RtoD":
        print("Radians ",valuen," to Degrees: ",math.degrees(valuen))
elif operation in raised:
    valuen=int(input("Enter the number: "))
    if sym == "root":
        print("Square root of ",valuen," is ",math.sqrt(valuen))
    elif sym == "sq.":
        print("Square of ",valuen," is ",math.pow(valuen,2))
    elif sym == "cu.":
        print("Cube of ",valuen," is ",math.pow(valuen,3))
    elif sym == "^":
        y=int(input("Enter the ",valuen," has to be raised to: "))
        print("Cube of ",valuen," is ",math.pow(valuen,y))
elif operation in extras:
    no1=int(input("Enter first numbers: "))
    no2=int(input("Enter second numbers: "))
    if sym == "/":
        dev=no1/no2
        print(no1,"/",no2,":",dev)
    elif sym == "-":
        dif=no1-no2
        print(no1,"-",no2,":",dif)
    elif sym == "+":
        print(no1,"+",no2,":",no1+no2)
    elif sym == "*":
        print(no1,"x",no2,":",no1*no2)
    elif sym == "rnd":
        random=[0,1]
        print(f"Result for list 1 using \"any\": \"{any(random)}\"")
    elif sym == "gcd":
        print(no1," and ",no2,":",math.gcd(no1,no2))