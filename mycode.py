"""
#q1
str = "gaurav kumar chauhan"
print(len(str))
print((str[ 1:-5]))

print(str.endswith("hn"))

print(str.capitalize())

print(str.count("a"))

print(str.find("z"))

print(str.index("a"))

print(str.isalnum())

print(str.isalpha())

print(str.isdigit())

print(str.islower())

print(str.isupper())

print(str.isspace())

print(str.istitle())

print(str.isprintable())

print(str.isidentifier())

print(str.isascii())

print(str.replace("gaurav kumar","riya"))

#Q3
name =input("enter your first name :")
print(name)
print(len(name))


#Q4
str = "Hi,i am $ gaurav$ kumar$ chauhan$"
print(str.count("$"))

#Q5
marks = int(input("enter your marks :"))

if (marks >= 90 and marks <= 100):
    print("A grade")
elif (marks >= 80 and marks < 90):
    print("B grade")
elif (marks >= 70 and marks < 80):
    print("C grade")
elif (marks >= 60 and marks < 70):
    print("D grade")
elif (marks >= 50 and marks < 60):
    print("E grade")
else:
    print("F grade")

#Q6
age = int(input("enter your age :"))
print(age)

if (age >= 18):
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

#Q7 NESTING
age = int(input("enter your age :"))

if (age >= 18):
    if (age >= 60):
        print("you are senior citizen")
    else:
        print("you are adult")
else:
    print("you are minor")

#Q8 wap to check if a number entered by user is even or odd

num = int(input("enter a number :"))
print(num)

if (num % 2 == 0):
    print("number is even")
else:
    print("number is odd")


#Q9 WAP to Find the largest of three numbers ENTERED BY USER

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter third number :"))

if (num1 > num2 and num1 > num3):
    print("largest number is :",num1)
elif (num2 > num1 and num2 > num3):
    print("largest number is :",num2)
else:
    print("largest number is :",num3)
    


    #Q10 WAP to check if a number is a multiple of 7 or not

num = int(input("enter a number :"))
print(num)

if (num % 7 == 0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")"""

