x=int(input("enter the number to find it i a factor"))
y=[]
print("the factor of",x,"are")
for i in  range(1,x):
    if x%i==0:
        y.append(i)
print(y)
print("no.of factor",len(y))
n=int(input("enter number"))
if n>len(y):
    print("invalid")
else:
    print("first",n,"factors")
    for k in range (0,n):
        print(y[k],end="")
