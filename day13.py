###Question 7
Num = input("Please input the number between 0 and 6=>")

if Num is "0":
    print("Sunday")
elif Num is "1":
    print("Monday")
elif Num is "2":
    print("Tuesday")    
elif Num is "3":
    print("Wednesday")
elif Num is "4":
    print("Thursday")
elif Num is "5":
    print("Friday")
else:
    print ("Saturday")

###Question 9
Child = int(input("Input Child num:"))
Adult = int(input("Input Adult num:"))
Senior = int(input("Input Senior num:"))

if Child+Adult+Senior>=10:
    total = Child*500+Adult*1000+Senior*700
    #print("Discount target!!! 20% OFF\n price is :"+str(total)+"*0.8="+str(total*0.8))
    print("Discount target!!! apply 20% OFF\n price is :{}*0.8={}".format(total,total*0.8))
else:
    total = Child*500+Adult*1000+Senior*700
    print("price is :"+str(total))

###Question 8
Year=int(input("which year doyou check?=>"))

if Year%400==0:
    print("leap year")
elif Year%4==0 and Year%100==0:
    print("not leap year")
elif Year%4==0:
    print("leap year")
