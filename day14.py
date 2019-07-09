#Crate simple calculator
def cal(x,y,z):
    if z==1:
        return x+y
    elif z==2:
        return x-y
    elif z==3:
        return x*y
    elif z==4:
        return x/y
    else:
        print("unexcepted value... done")
while True:
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2st number : "))
    print("[1]addition\n[2]subtraction\n[3]multiplication\n[4]divitsion")
    while True:
        z=int(input("What operator? "))
        if z>=1 and z<=4:
            ans = cal(x,y,z)
            print("Answer is : ",ans)
            break
        else:
            print("unexcepted value.Please retry")
