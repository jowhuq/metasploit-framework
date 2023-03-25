def arm(x):
    temp=x
    res=0
    while x!=0:
        n=x%10
        res+=n**3
        x//=10
    if res== temp:
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")

x=int(input("Enter the number="))
arm(x)
