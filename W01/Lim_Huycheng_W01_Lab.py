#exercise 1 
print("Excercise 1 : Perform 4 operations(+ / - / * / \ )")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("Sum:",num1 + num2)

print("Different:",num1 - num2)

print("Product:",num1 * num2)

print("Quotient:",num1 / num2)

#excercise 2
print("Excercise 2 : Find the largest number")
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))

if(n1 > n2 and n1 > n3):
    print("The largest number is:" , n1)
elif(n2 > n1 and n2 > n3):
    print("The largest number is:" , n2)
elif(n3 > n1 and n3 > n2):
    print("The largest number is:" , n3)
else:
    print("There's no largest number")

#excercise 3
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)

#excercise 4
print("Excercise 4 : Factorial")
take = int(input("Enter a number:"))
fact = 1
for x in range  (1 , take+1):
    fact = fact * x
print ("Factorial of" , take , "is", fact)

#excercise 5 
print("Excercise 5 : Check whether it's a palindrome or not")
string = input("Enter a string:")
slicing = string[::-1]

if (string == slicing):
    print(string,"is a palindrome")
else:
    print(string,"is not polindrome")
 
#Bonus
print("Excercise 6 : Check password")
pw = str(input("Enter a password to check its strength:"))
check_len = len(pw)

special_cha = "!@#$%^&*()"
has_lowercase = False
has_uppercase = False
has_number = False
has_special = False

if check_len < 8:
    print("Weak")
else:
    for char in (pw):
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_number = True
        elif char in special_cha:
            has_special = True
    if has_lowercase and has_uppercase and has_number and has_special:
        print("Strong")
    else:
        print("Moderate")



    



        


