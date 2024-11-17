#excercise 1 
class Car:
    def __init__(self , make , name , model):
        self.make = make
        self.name = name
        self.model = model
    def display_info(self):
        print("Car: " , self.make)
        print("Car: " , self.name)
        print("Car: " , self.model)

my_car = Car("Toyota" , "Corolla" , 2020)
my_car.display_info()
print("\n")

# excercise 2
from datetime import datetime
print("Excercise 2")
class Car:
    # make = "Toyota"
    # model = "Corolla"
    # year = 2020
    def __init__(self , make , model , year):
        self.make = make
        self.model = model
        self.year = year
    def is_vintages(self):
        now = datetime.now().year
        return (now  - self.year) > 25 

one_vintages = Car("Toyota" , "BMW" , 1990)
non_vintages = Car("wr" , "corolla" , 2024)
print("Car 1 is vintage: " , non_vintages.is_vintages())
print("Car 2 is vintage: " , one_vintages.is_vintages())
print("\n")
# excercise 3
print("Excercise 3 ")
class Student:
    name = 'Jonh'
    age = 20
    grade = 'B'
    def update_grade(self , new_grade):
        self.grade = new_grade

update = Student()

print("Before grade update:")
print("Name: " , update.name)
print("Age: " , update.age)
print("Grade: " ,update.grade)
print("\n")
print("After grade updated:")
out = update.update_grade ("A")
print("Name: " , update.name)
print("Age: " , update.age)
print("Grade: " , update.grade)
print("\n")

# excercise 4
class BankAccount:
    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance
        print(f"Initial balance for {owner}: {balance}")
    def deposit(self , amount):
        #self.amount = amount
        self.balance += amount
        
        print("\n")
        print(f"Deposit : ${amount}")
        print(f"New balance: ${self.balance}")

    def withdraw(self , amount):#no need to create attibute amount 
        self.amount = amount
        self.balance -= self.amount
        print("\n")
        print(f"Withdraw: ${amount}")
        print(f"New balance: ${self.balance}")
        print("\n")
#no need to create new function attemping, add condition in withdraw
    def attempting(self, attempting):
        print(f"Attempting to withdraw ${attempting}")
        if attempting > self.balance:
            print("Insuffient funds. Withdrawl Failed.")
        else:
            print("Withfraw Successed.")

        print(f"Final Balance: ${self.balance}")

    
user_balance= BankAccount("Jonh" , 1000)
user_deposit = user_balance.deposit(500)
user_withdraw = user_balance.withdraw(300)
attempting = user_balance.attempting(2000)
print("\n")
# excerise 5

class Book:
    def __init__(self, title, author ,price ):
        self.title = title
        self.author= author
        self.price = price

class Library(Book):
    def __init__(self):
        self.books = [] #list of books object

    def add_book(self,book):
        self.books.append(book)

    def show_books(self):
        print("Book in the library:")
        #enumerate function syntax: (list , start index)
        for index , book in enumerate(self.books ,1):
            print(f"{index}. Title: {book.title}, Author: {book.author} , Price: {book.price}" )
#===========================================================================================================

library = Library()
book1= Book("The great man," , "F. Ane Fit," , 10.99)
book2 = Book("The Story about APT," , "Fake Men," , 12.50)
book3= Book(1984 , "George OrWell," , 9.75)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.show_books()
print("\n")

#excerise 6
class ClassRoom:
    def __init__(self, class_name):
        self.calss_name = class_name
        self.students = [] #list students 
        
    def add_student(self, name):
        self.students.append(name)
        print(f"Added student: {name}")

    def list_students(self):
        print(f"Students in {self.calss_name}")
        for i in self.students:
            print("-", i)

classroom = ClassRoom("Math 101")
classroom.add_student("Alice")
classroom.add_student("Bob")
classroom.add_student("Charlie")
classroom.list_students()
print("\n")
# excerise 7
class PhoneBook():
    def __init__(self):
        self.contact = {}
    def add_contact(self, name, number):
        self.contact[name] = number 
        print(f"Added Contact: {name} -> {number}")
    def find_contact(self, name):
        self.name = name
        if name in self.contact:
            print(f"{name}'s number: {self.contact[name]}")
        else:
            print(f"{name} not found in phone book.")
phone = PhoneBook()
phone.add_contact("Jonh","123-456-7890")
phone.add_contact("Jane","987-654-3210")
phone.find_contact("Jonh")
phone.find_contact("Alice")
print("\n")
# excercise 8
class SportsLeague:
    def __init__(self):
        self.teams = {}  # Dictionary where keys are team names, values are lists of player dictionaries
    def add_team(self, team_name):
        # Write your code here
        if team_name not in self.teams:
            self.teams[team_name] = []
            print(f"Team '{team_name}' added.")
        else:
            print("User already exited.")
    def add_player(self, team_name ,player_id , player_name, position):
        # Write your code here
        # player_infor = {}
        if team_name in self.teams:
            if any(player['player_id'] == player_id for player in self.teams[team_name]):
                print(f"{self.player_name} Already in '{team_name}'")
            else:
                player_infor= {'player_id': player_id, 'player_name': player_name, 'player_position': position}
                self.teams[team_name].append(player_infor)
                print(f"Player' {player_name}' added to team '{team_name}'.")
        else:
            print("Team doesn't exits.")

    def view_team(self, team_name):
        # Write your code here
        if team_name in self.teams:
            player_infor = self.teams[team_name]
            if player_infor:
                print(f"Team '{team_name}' players:")
                for player in player_infor:
                    print(f"ID:{player["player_id"]}, Name: {player["player_name"]} , Position: {player["player_position"]}")
            else:
                print(f"Team '{team_name}' is empty") 
        else:
            print(f"Team '{team_name}' doesn't exist. ")         


    def update_player(self, team_name, player_id, new_name=None, new_position=None):
        # Write your code here
        for player in self.teams[team_name]:
            if player_id == player["player_id"] :
                player["player_name"] = new_name
                if new_name:
                    player["player_name"] == new_name
                if new_position == player["player_position"]:
                    player["player_position"] == new_position
                return print(f"Player ID {player_id} updated to team '{team_name}'.")
            return print("Player's ID not found.")
        else:
            print("Team doesn't exist.") 

    def remove_player (self, team_name, player_id):
        # Write your code here
        if team_name in self.teams:
            for i, player in enumerate(self.teams[team_name]):
                if player["player_id"] ==  player_id :
                    remove = self.teams[team_name].pop(i)
                    print(f"Player: '{remove["player_name"]}' removed from team '{team_name}'.")
                    return 
            print(f"Player ID {player_id} not found in team '{team_name}'")
        else:
            print(f"Team '{team_name}' doesn't exist.")



# Example Usage:
league = SportsLeague()

# Adding teams
league.add_team("Tigers")
league.add_team("Sharks")

# Adding players
league.add_player("Tigers", 1, "John Doe", "Forward")
league.add_player("Tigers", 2, "Alice Smith", "Goalkeeper")
league.add_player("Sharks", 3, "Bob Brown", "Defender")

# # Viewing teams
print("\nViewing teams:")
league.view_team("Tigers")
league.view_team("Sharks")

# Updating a player's information
print("\nUpdating player info:")
league.update_player("Tigers", 1, new_name="Johnny Doe", new_position="Striker")
league.view_team("Tigers")

# Removing a player
print("\nRemoving a player:")
league.remove_player("Tigers", 2)
league.view_team("Tigers")




        
