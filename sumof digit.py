n=int(input("enter th three digit numer"))
s=0
temp=n
while temp>0:
    digit=temp%10
    s+=digit
    temp=temp//10
print("sum of given number is ",s)
