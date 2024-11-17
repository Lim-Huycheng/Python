if 5 > 2:
    print("5 is greater than 2! ")
    print("Hi false?")

#This is how we can comment in Python
"""
    Other approach to comment in Python programming

    print("Hello"   )
"""

x = 5
x = "String"
y = "Cheng"
print(x,y)

#Specify the data types
x = int(3)
y = str(9)
z = float(5)

#To know the type of each Variables

print(type(x),type(y),type(z))

my_var = 'cheng'

#Unpacking

fruits = ["apple" , "banana" , "cherry"]
x , y , z = fruits
print(x,y,z)

#concat the output

x = 'Hi'
y = " thisis"
z = "Cheng!!!"

print(x + y + z)

x = 'Awesome'
def myfunc():
     # value of x is Local
     x = 'Loy nas'
     print("Python is " + x )

myfunc() 
print(x)

#We can also used Global in Function

def myglobal():
    global x 
    x = 'WOW'
    
myglobal()

print("Python is " + x)

a = 2.5

print(a)


#Complex 
# j in complex is Imaginary part
x = 3+5j
y= 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1
print(x)
a = float(x)
print(a)
#You can't convert compoex number to another number type

import random
print(random.randrange(1,10))

import math
math.pi
print(math.pi)

#length
s ='spam'
#len(str(s))
print(len(s[-1]))
s.find("pa")
print(s.find("pa"))


s.replace('pa', 'x')
print(s.replace)

for x in 'banana':# x = banana if true print banana
    print(x)


#Check String
txt = 'lim huycheng'
print('lim' in txt) # means: lim is in txt or not? we can use to seach sth some words in the full words.
#Upper fucntion

a= 'CHENG'
print(a.lower())

#Replace Method
a= "O Sl B"
print(a.replace('O' , 'B'))

#Split Method
b = "Damn, I love you!!!"
print(b.split("I")) #I isn't display 

c = a + b
print(c)

age = 9
txt = f"This is age {age}"
print(txt)

txt =f"The mulitiplication of {20 * 40}"
print(txt)

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(M[2])
print(M)
print(M[2][2])

row = [row[1] for row in M if row[0] % 2 == 0 ]

print(row)

sum = [23,13,56,78,98,99,100]

G = (sum(row) for row in M)
print(G)


input = input("Enter Your Name: ")
print("your name is" + input + ".")

l = ["Name" , 123 , "spam"]
# len(l)
print(len(l))
print(l[2])

#Bounds Checking
#Dictionary

D = {'Food': 'Apple', 'Book': 'LingOrm', 'Car': 'BMW', 'Quantity': 2}
D['Quantity'] += 1
print(D)

#Nested Revisited

rec = {'name': { 'First': 'LingLing', 'Last': 'Kwong'}
       , 'job': 'CyberSecurity' , 'age' : 20}
print("print\n")
print(rec['name'], rec['job'] , rec['age'])

if 'name' in rec:
    print('Not Missing')

#  IF NOT used to reverse the result 
i = 100
j = 200
if not j < i:
    print('Correct') 
    







