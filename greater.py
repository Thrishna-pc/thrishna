a=int(input("enter number1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))
if((a>b) & (a>c)):
    {
        print(a, "is greatest")
    }

elif((b>a) & (b>c)):
    {
        print(b, "is greater")
    }
elif((c>a) & (c>b)):
    {
        print(c, "is greatest")
    }
else:
    {
        print("doing math make me feel dizzy, please leave me alone!")
    }
