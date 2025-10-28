#square of given number number
def square():
    a=int(input("enter a number to get a square"))
    b=a**a
    print(b)
#cube of given number
def cube():
    a=int(input("enter a number to get a cube"))
    b=a**3
    print(b)
# to convert celsius to farenheit
def ctof():
    a=float(input("enter celsius value to get farenheit"))
    b=(9/5*a)+32
    print(f"{a}is converted to {b}")
# to convert farenheit to celsius
def ftoc():
     a=float(input("enter farenheit value to get celsius"))
     b=(a-32)*5/9
     print(f"{a}is converted to{b}")
ftoc()
