
"""#Q1 str slicing or functions
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

print(str.replace("gaurav kumar","riya"))"""

"""

#Q3
name =input("enter your first name :")
print(name)
print(len(name))
"""
"""

#Q4
str = "Hi,i am $ gaurav$ kumar$ chauhan$"
print(str.count("$"))
"""
"""
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
"""
"""
#Q6
age = int(input("enter your age :"))
print(age)

if (age >= 18):
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")
"""

"""
#Q7 NESTING
age = int(input("enter your age :"))

if (age >= 18):
    if (age >= 60):
        print("you are senior citizen")
    else:
        print("you are adult")
else:
    print("you are minor")
"""


"""
#Q8 wap to check if a number entered by user is even or odd

num = int(input("enter a number :"))
print(num)

if (num % 2 == 0):
    print("number is even")
else:
    print("number is odd")

"""


"""
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
    

"""

"""
    #Q10 WAP to check if a number is a multiple of 7 or not

num = int(input("enter a number :"))
print(num)

if (num % 7 == 0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")

"""

"""
#list in python
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
#etc"""

"""

#tuple
tuple = (43,655,96,327,975,8945,9)
#tuple[0],tuple[1],tuple[2]
tuple[1]=65 #not allowed
#list is mutable and tuple is not mutable we can not b

#tuple slicing is same as list slicing
print(tuple[1:4])
#tuple methods
print(tuple.count(43)) #count the occurance of element
print(tuple.index(43)) #return the index of element
print(len(tuple)) #return the length of tuple
print(max(tuple))
print(min(tuple))
print(sum(tuple))
"""


"""
#Q11 wap to ask user to enter names of their 3 favourite  movies & store them in a list 

a = input("enter your first favourite movie :")
b = input("enter your second favourite movie :")
c = input("enter your third favourite movie :")

movies = [a,b,c]
print(movies)

#or

movies = []
movies.append(input("enter your first favourite movie :"))
movies.append(input("enter your second favourite movie :"))
movies.append(input("enter your third favourite movie :"))
print(movies)

#or

movies = []
for i in range(3):
    movies.append(input("enter your favourite movie :"))
print(movies)


"""


"""
#Q12 wap to check if a list contains a palindrome of elements.(hint: use copy() method)

list = [1,2,3,2,1]
list1 = list.copy()
list1.reverse()

#or

list = [1,2,3,2,1]
list1 = list[::-1]

if (list == list1):
    print("list contains palindrome")
else:
    print("list does not contain palindrome")
"""


"""
    #Q13 wap to count the number of students with the "A" grade in the following tuple

    z = ("A","B","A","C","A","D","A","E","A","F","A","G","A","H","A","I","A","J","A","K","A","L","A","M","A","N")
    print(z.count("A"))

    #STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM A TO Z
    z = ("A","B","A","C","A","D","A","E","A","F","A","G","A","H","A","I","A","J","A","K","A","L","A","M","A","N")

    list.sort()

    print(list)

    #or

    list = list(z)
    list.sort()
    print(list)
"""


"""
#dictionary in python

info ={
    "name":"gaurav",
    "age":22,
    "phone":7453093954,
    "city":"up",
    "email":"gaurav745309@gmail.com",
    
    "subjects": ["python","cpp","java","dsa"]
}
print(info["age"])
print(info["name"])
print(info["phone"])
print(info["city"])
print(info["email"])

info["age"]=23 #we can change or modify our values
print(info["age"])

info["address"]="delhi"#we can assign a new key value pair
print(info)

null_dict = {}
print(null_dict)
print(type(null_dict))
null_dict["name"]="gaurav"
null_dict["age"]=22
"""


"""
#nested dictionary in python
#dictionary inside dictionary or list inside dictionary or dictionary inside list

info ={
    "name":"gaurav",
    "age":22,
    "phone":7453093954,
    "city":"up",
    "email":"gc790093@gmail.com",
    "subjects": ["python","cpp","java","dsa"],
    "address":{
        "street":"xyz",
        "city":"delhi",
        "state":"delhi",
        "pin":110085
    }
}
print(info["address"]["city"])
print(info["address"]["state"])
print(info["address"]["pin"])
"""

"""
#dictionary methods
print(info.keys()) #to print all keys
print(list(info.keys())) #use type cast to modify our values
print(len(list(info.keys()))) # print length 
print(info.items()) #to print all key pair values
print(info.values()) #to print all values
print(info.get("name")) #to get the value of key
print(info.pop("name")) #to remove the key value pair
print(info)
print(info.update({"name":"gaurav"})) #to update the value of key

new_info = { "name":"gaurav","age":22,"phone":7453093954,"city":"up",}

print(info.update(new_info))
print(info)
"""

"""
#set in python
#set is a collection of unique elements
#set is unordered
#set is mutable
#set does not support indexing
#set does not support slicing
#set does not support duplicate elements
#set is represented by {}
#set is not hashable
#set does not support list or dictionary as an element of set but it supports tuple as an element of set because tuple is hashable and list is not hashable and dictionary is not hashable and set is not hashable and set does not support hashable elements
#repeatation of elements is not allowed in set
null_set = set() #empty set
#set is diffrent as compared to dictionary because set does not have key value pair and dictionary has key value pair


set = {1,2,3,4,5,6,7,8,9,0}
print(set)
print(type(set))
print(len(set))

sooot = {}
print(type(sooot)) #it is dictionary not set because set is represented by {} and dictionary is also represented by {} so we can not create empty set like this we have to use set() function to create empty set
sooot.add() #to add element in set
sooot.remove() #to remove element from set
sooot.discard() #to remove element from set
sooot.clear() #to clear the set
sooot.copy() #to copy the set
sooot.pop() #to remove the random element from set
sooot.union() #to combine two sets
sooot.intersection() #to find common elements in two sets
sooot.difference() #to find the difference between two sets
sooot.symmetric_difference() #to find the symmetric difference between two sets
sooot.update() #to update the set
set.add(1)
print(set)
set.add(2)
print(set)
set.add(3)
print(set)
"""

"""
gaurav = (1,2,3,4,5,6,7,8,9,0,'hello','world','gaurav','kumar','chauhan')
print(gaurav)
gaurav = set()
gaurav.add(1)
gaurav.add(2)
print(gaurav)
print(type(gaurav))
gaurav.add(1)
#set is mutable but it does not support duplicate elements and its element is immutable so we can not change the element of set and does not take dict or list as an element of set
"""

"""
myname = set()


myname.add('gaurav')
myname.add('kumar')
myname.add('chauhan')
print(myname)
print(type(myname))
myname.add((1,2,3,4,5,6))
print(myname)
#myname.add([1,2,3,4,5,6]) #not allowed because list is mutable and set does not support mutable elements"

"""


"""
collection = set()
collection.add("gaurav")
collection.add("kumar")
collection.add("chauhan")
print(collection.pop())
print(collection)"
"""

