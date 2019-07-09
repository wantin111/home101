##Day2 Question1.
name = "Yuji Ogawa"
age = 28
intro = ("My name is "+name+". I’m "+str(age) +" years old.")
print(intro)

##Day2 Question2.
weight = int(input("Input your weight(kg)"))
height = float(input("Input your height(m)"))
bmi = weight/(height*height)
print(bmi)

##Day2 Question3.
students =  ["ichiro","jiro","saburo","siro","goro"]
print(students[0])
print(students[1:4])
#print(students[-4:-1])  

##Day2 Question4.
student = {"ichiro":167,"jiro":157,"saburo":180,"siro":176,"goro":167}
a = input("input student name=")
print ("The student hight is" +str(student[a]))

##Day2 Question5.
# box=[]
# ichiro ={"math":80,"English":60,"sciece":77}
# jiro ={"math":80,"English":60,"sciece":77}
# saburo ={"math":80,"English":60,"sciece":77}

# box.append(ichiro)
# box.append(jiro)
# box.append(saburo)
# print(box)