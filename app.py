#In operator
my_answer = "rock"
options = ['rock', 'paper', 'scissors']

if my_answer in options :
    print('Rock is one of the possible options')

my_answer = input("What is the answer")
option = ['rock', 'paper', 'scissors']
if my_answer in option :
    print("The answer is viable option")
else:
    ("Wrong answer, try again")  


key = "name"
person = {
    "name" : "Kalob",
    "profession" : "teacher",
}

if key in person:
    print("name is a valid directory and key is person object")


    # Not operator
    my_thing = False
    if not my_thing:
        print("print a statement here")

name1 = 'Kane'
name2 = 'Kalob'
if name1 != name2:
    print("different names") 


# function inside a function

def thing1():
    print("Welcome thing one")

    def thing2():
        print("Welcome thing2")

thing1()


def names(name):
    print(f"welcome {name}. You can have a sit")

    def name1(name):
        print(f"welcome {name}. Take a sit. Thank you")
names("John")  


def add_num(args):
    print(args)
    print(type(args))

add_num(1)


def names(name, *args):
    print(args)
    print(type(args))

names("John", 2, 3)  


def add_numbs(*args):
    total = 0
    for num in args:
        total = total + num
        return total
total = add_numbs(1, 2, 5)    
print(total)

# Function **Kwargs(key word arguement)

def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("you are", kwargs.get("age"))

person(name='John', age=37, height='160cm')


def order_pizza(name, address, **toppings):
    print(f"order is for {name}")
    print(f"order is for {address}")

    price = 18.00
    for key, value in toppings.items():
        price = price + 2
        print(f"your total price is {price}")
        return price

order_pizza("Amanda", "Canada", Jalepano= True, extra_cheese= True, ham =True)

names = ['alex', 'john', 'grace', 'amanda']
names.append('Rhauby')
print(names)

names.remove('alex')
print(names)

    
# List enumeration
animals = ['Lion', 'Dog', 'Cat', 'Goat']
for animal in enumerate (animals) :
    print(animal)       





    