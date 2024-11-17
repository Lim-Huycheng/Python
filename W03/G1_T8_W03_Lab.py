''' G1-T8:
    1. Lim Huycheng
    2. Chhorn Esaranarin
'''
print("G1-T8:")
print("1. Lim Huycheng")
print("2. Chhorn Esaranarin")
print("\n")
#Roman 1 Excercise 1
print("I")
print("Excercise 1\n")
print("Write a for loop that prints each element in the list numbers = [1, 2, 3, 4, 5].\n")
# Creating for  loop to print each element in the list numbers
for i in range(1, 6):
    print(f"Number: {i}")
print("\n")

# Roman 1 excercise 2
print("Excercise 2\n")
print("Create a while loop that counts from 1 to 10 and prints the numbers. Use break to exit the loop when the count reaches 6.\n")
# Create a variable
count = 1
#Using while loop
while count <= 10:
    if count == 6:
        break # Using break to stop the loop it reach number we want.
    print(f"Count: {count}")
    count += 1

print("\n")

# Roman 1 Excercise3
print("Excercise 3\n")
print("Modify the previous while loop to use continue to skip printing the number 4.\n")
# Create a variable
Num = 1
#Using while loop
while Num <= 10:
    if Num == 4:
        Num += 1
        continue # Using break to stop the loop it reach number we want.
    print(f"Number: {Num}")
    Num += 1
print("\n")

#Roman 2 Excercise 1
print("II")
print("Excercise 1\n")
print("Create a list of your favorite fruits and print it.")
fav_fruit = ["Watermelon" , "Banana" , "Grape","Durian" , "Guava"]
print(fav_fruit)
print("\n")

#Roman 2 Excercise 2
print("Exercise 2\n")
print("Add a new fruit to the list using the append method and print the updated list.")
fav_fruit.append("Rambutan")
print(fav_fruit)

print("\n")


#Roman 2 Excercise 3
print("Excercise 3\n")
print("Remove a fruit from the list using the remove method and print the updated list.")
fav_fruit.remove("Grape")
print(fav_fruit)
print("\n")
#Roman 2 Excercise 4
print("Excercise 4\n")
print("Sort the list in alphabetical order and print it.")
fav_fruit.sort()
print(fav_fruit)
print("\n")

# Roman 3 Excercise1
print("III")
print("Excercise 1\n")
print("Create a tuple containing five integers and print it.")
my_tuple = (1,2,3,4,5)
print(my_tuple)
print("\n")

# Roman 3 Excercise2
# print(" Excercise 2 Attempt to change one of the integers in the tuple (this should raise an error.")
# my_tuple1 = (1,2,3,4,5)
# my_tuple1[0] = 6
# print(my_tuple1)
# print("\n")

# Roman 3 Excercise3
print("Excercise 3\n")
print("Convert the tuple into a list and print the list.")
my_tuple2 = (1,2,3,4,5)
convert_to_list = list(my_tuple2)
print("Convert tuple to list: " , convert_to_list)
print("\n")

#Roman 4 Excercise1
print("IV")
print("Excercise 1\n")
print("Create a dictionary to store the ages of three people (e.g.,Alice: 30, Bob: 25, Charlie: 35) and print it.\n")
# Create a varible to store ages of three people
age_of_people = {"Alice": 30, "Bob": 25, "Charlie": 35}
print(age_of_people)
print("\n")


# Roman 4 Excercise2
print("Excercise 2\n")
print("Add a new person to the dictionary and print the updated dictionary.")
# Create a varible to store ages of three people
age_of_people = {"Alice": 30, "Bob": 25, "Charlie": 35}
age_of_people.update({"John": 40})
print(age_of_people)
print("\n")


# Roman 4 Excercise3
print("Excercise 3\n")
print("Remove one person from the dictionary using the pop method and print the updated dictionary.\n")
# Create a varible to store ages of three people
age_of_people = {"Alice": 30, "Bob": 25, "Charlie": 35}
age_of_people.pop("Charlie")
print(age_of_people)
print("\n")


# Roman 4 Excercise4
print("Excercise 4\n")
print("Print all keys and values in the dictionary using a loop.")\
# Create a varible to store ages of three people
age_of_people = {"Alice": 30, "Bob": 25, "Charlie": 35}
for x, y in age_of_people.items():
    print(x, y)
print("\n")


#Roman 5 
print("V")
print("Excercise 1\n")
print("Write a function named add that takes two numbers as arguments and returns their sum.")
def add(num1 , num2):
    return num1 + num2

out_put = add(1,2)
print("The result :", out_put)

print("Excercise 2\n")
print("Create a function named greet that prints without returning a value.")
def greet():
    print("Hello, World!")
#call the function without returning a value
greet()
print("\n")

print("Excercise 3\n")
print("Write a lambda function that takes one argument and returns the square of the number.use it to print the square of 5.")
x = lambda a : a**2 
print("The result of square of 5:" , x(5))
print("\n")

print("Bonus Exercise")

import re

username_list = []
user_data = {}

def register():
    username = input("Enter a username: ")

    # Using a while loop to ensure correct password format
    while True:
        user_pw = input("Enter a password: ")
        
        if len(user_pw) < 8:
            print("Password too short. Must be at least 8 characters.")
            continue
        if not re.search(r"[A-Z]", user_pw):
            print("Password must contain at least one uppercase letter.")
            continue
        if not re.search(r"[0-9]", user_pw):
            print("Password must contain at least one digit.")
            continue
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", user_pw):
            print("Password must contain at least one special character.")
            continue  
        
        print("Registration successful with a strong password!")
        username_list.append(username)
        user_data[username] = user_pw
        return

def login():
    attempts = 3
    user = input("Enter your username: ")
    
    if user in username_list:
        while attempts > 0:
            pw = input("Enter your password: ")
            if pw == user_data[user]:
                print(f"Login Successful! Welcome, {user}")
                return
            else:
                attempts -= 1
                print(f"Invalid credentials. You have {attempts} attempts left.")
                
        print("Too many login attempts. Access denied.")
    else:
        print("Invalid Username. Please try again!")

def forgot_pw(): 
    username = input("Enter your username to retrieve your password: ")
    if username in user_data:   
        print(f"Your password is: {user_data[username]}")
    else:
        print("This user doesn't exist.")

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

while True:
    print("\nWelcome to the Bonus Point Exercise")
    print("1. Register")
    print("2. Login")
    print("3. Forgot password")
    print("4. Exit")
    
    try:
        op = int(input("Choose your option (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    
    if op == 1:
        register()
    elif op == 2:
        login()
    elif op == 3:
        forgot_pw()
    elif op == 4:
        exit_program()
    else:
        print("Invalid option. Please try again.")
