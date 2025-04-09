
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

"""
set1 = {'a','b','c','d',1,2,3,4,5,6}
set2 = {'d','e','f','g',4,5,6,7,8,9}

print(set1.union(set2))  # combine both and single time print all unique values
print(set1.intersection(set2)) #print common elements in both sets"
"""
    
#store following word meaning in a python dictonary
"""
dictionary = {
    "cat" : "a small animal",
    "table" : ["a peice of furniture","list of facts & figures"]
}

print(dictionary)

classroom = {"python","cpp","java","dsa","javascript","html","css","sql","c","c++","python","cpp","java","dsa","javascript","html","css","sql","c","c++"}
print(len(classroom))
print(classroom)

#Q14 WAP to enter marks of 5 subjects from user and store them in a dictionary.starting with an empty dictionary & add one by one. use subject name as a key & mark as value.

marks = {}
marks["maths"] = int(input("enter your maths marks :"))
marks["science"] = int(input("enter your science marks :"))
marks["english"] = int(input("enter your english marks :"))
marks["hindi"] = int(input("enter your hindi marks :"))
marks["sst"] = int(input("enter your sst marks :"))
print(marks)

#or

marks = {}

x = int(input("enter your maths marks :"))
marks.update({"maths":x})

x = int(input("enter your science marks :"))
marks.update({"science":x})

x = int(input("enter your english marks :"))
marks.update({"english":x})

x = int(input("enter your hindi marks :"))
marks.update({"hindi":x})

x = int(input("enter your sst marks :"))
marks.update({"sst":x})

print(marks)"""
"""
#Q15 figure out a way to store 9 & 9.0 as separate elements in a set

values = {9,9.0}
print(values)

#or

values = set()
values.add(9)
values.add(9.0)
print(values)

#or

values = {9,"9.0"}
print(values)

#or

values = {
    ("float",9.0),
    ("int",9)
}
print(values)"""

# loops in python
# for loop
# while loop
# nested loop
# infinite loop
# loop control statements
# break
# continue
# pass
# loop else
# nested loop else

#loops are used to repeat instructions or statements
#loops are used to iterate over a sequence

# while loop

#while condition:
#    statements
"""
print("hello world!")
print("hello world!")
print("hello world!")
print("hello world!")
print("hello world!")"""
"""
count = 0
while count <= 6 :
    print("hello world!")
    count += 1;
    print(count)

    #here count is iterator and it is used to iterate over the sequence
    #count is used to count the number of iterations
    #in loop statement is iterational statement"""
"""
i = 0
while i < 6:
   
    i += 1
    print(i)

    #Q1 print numbers from 1 to 100

i = 0
while i < 100:
    i += 1
    print(i)
   

    #Q2 print numbers from 100 to 1
    i = 100
    while i >= 1:
        i -= 1
        print(i)
       """
#Q3 input a number from user and print its table
"""n = int(input("enter a number :"))
i = 0
while i < 10:
    
    i += 1
    print(i*n)"""
#Q4 print the elements of list using while loop
#list = [1,4,9,16,25,36,49,64,81,100]

"""i = 1
while i<=10:
    print(i*i)
    i += 1

    #list = [100,81,64,49,36,25,16,9,4,1]

i = 10
while i >= 1:
    print(i*i)
    i -= 1

#searching for a nmber x in this tuple using loop
#tuple = (1,4,9,16,25,36,49,64,81,100)

x = 25
tuple = (1,4,9,16,25,36,49,64,81,100)
i = 0
while i < len(tuple):
    if tuple[i] == x:
        print("element found at index :",i)
        break
    i += 1
    break"""
"""str = "gauravkumarchauhan"
for char in str:
    print(char)
    else:
        print("no character left")"""
    
"""nums = (1,4,9,16,25,36,49,64,81,100,25)
x = 25

idx = 0
for el in nums:
   if(el == x) :
         print("element found at index :",idx)
   idx += 1"""
       

"""for el in range(8):
    print(el)

for el in range(1,8):
    print(el)

for el in range(1,1445,21):
    print(el)"""
"""    
for el in range(8*8,300,66):
    print(el)"""

"""def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    #print("END")

show(990)"""
"""
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    

print(fact(6))"""

"""def sum(n):
    if(n==0):
     return 0
    else:
       return sum(n-1)+(n)
    
print(sum(67))"""


#write a recursive function to print all elements in a list
#hint : use list & index as a parameter

"""def _list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    _list(list,idx+1)

vegetable =["ladyfinger","pumpkin","carrot","pea","lemon"]
_list(vegetable)"""




#file/io

"""f = open("practice.py","r")
data = f.read()
print(data)
print(type(data))
f.close()

"""

"""f =open("open.txt","w")
f.close()
import os
os.remove("open.txt") #delete a file"""
"""
f = open("practice.txt","a+t")

f.write("hi everyone\n we are learning file I/O\n using java.\n I like programming in java")

with open("practice.txt","r") as f:
    data = f.read()
    #to replace the word java with python in the file
new_data = data.replace("java","python")
with open("practice.txt","w") as f:
    f.write(new_data)
"""
"""
#to find a word in a file
def find_word_in_file(file_path, word):
    word = "python"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("word found")
        else:   
            print("word not found")
            
            
            
            find_word_in_file("practice.txt","python")"""

"""def check_for_line():
    word = "java"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print("line no : ",line_no)
                return
                line_no += 1
              
            return -1
print(check_for_line())
   """
count = 0
with open("practice.txt","r") as f:
    data = f.read()
 

# num = ""
   # for i in range(len(data)):
       # if (data[i]== " ," ):
          #  print(int(num))
         #   num = ""
       # else:
       #     num += data[i]

    nums = data.split(",")
    for val in nums:
       if(int(val) % 2 == 0):
           count += 1


print(count)