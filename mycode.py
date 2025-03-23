
#Q1
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
else:ti
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
    print("number is not multiple of 7"


marks = [54,4546,767,75,35,65]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(len(marks))


#student = ["gaurav",86,87,97,45,66,33, 7453093954,"up"]
#print(student[8])
student=[45,67,546,6,6,6,68,9,9,6,554,4,5,4667,89,99,9,8,7]

#slicing
print(student[1:4])
print(student[1:])
print(student[1:len(student)])
print(student[:4])
print(student[-3:-1])
student.append(78)
#add one element at the end
print(student)
student.sort()#short in assending order
print(student)
student.sort(reverse=True)#sorts in desending order
print(student)
student.reverse()
#print(student.insert(index,element)) #insert element at index
print(student)
student.remove(1) #remove first occurrance of elements
print(student)
student.pop(5) #remove element at idx 
print(student)
#etc

#tuple
tuple = (43,655,96,327,975,8945,09)
#tuple[0],tuple[1],tuple[2]
tuple[1]=65 #not allowed
#list is mutable and tuple is not mutable we can not b

#tuple slicing is same as list slicing
print(tuple[1:4])
#tuple methods
print(tuple.count(43))
print(tuple.index(43))
print(len(tuple))
print(max(tuple))
print(min(tuple))
print(sum(tuple))"""

#Q11 wap to ask user to enter names of their 3 favourite  movies & store them in a list 

a = input("enter your first favourite movie :")
b = input("enter your second favourite movie :")
c = input("enter your third favourite movie :")

movies = [a,b,c]
print(movies)

""""""
