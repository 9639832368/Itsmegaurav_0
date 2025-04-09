"""cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
heros = ["thor", "ironman", "spiderman", "batman", "superman"]
# Print the list of cities

def print_list(list):
    for city in list:
        print(city, end="\n")
    print(len(cities))

print_list(cities)"""

"""def facto(n):
   # num = n
    fact = 1
    for i in range(1, n+1):
        fact *=i
        print(fact)
facto(7)"""

"""def value_convert(usd):
    inr_val = usd*83.78

    print(usd, "usd = ",inr_val , "inr ")

value_convert(55)"""

"""def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


even_odd(90)"""
"""
class student:
    def __init__(self, name,history, geography, english):
        self.name = name
        self.history = history
        self.geography = geography
        self.english = english




    def avg(self):
       print((self.history + self.geography + self.english) / 3)

s1 = student("John", 90, 80, 85)
  s1.avg()
"""
class account:
    def __init__(self, balance,account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("New balance is ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("New balance is ", self.balance)

    def check_balance(self):
        

        print("Current balance is ", self.balance)

acc1 = account(1000, 1234567890)
acc1.credit(500)
acc1.debit(200)
acc1.credit(100000)

acc1.check_balance()