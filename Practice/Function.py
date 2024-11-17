"""
def func(name,age):
    #print(name,age)

func('Jonh', 10)

def func1(*args):
    for i in args:
        print(i)

func1(20,40,60)
func1(80 , 100)

def calculation(a , b):
    sum = a + b 
    sub = a - b
    return sum , sub

res =calculation(40,10)
print(res)

def showEmployee(name , salary=9000):
      print("Name:",name,"salary:",salary)

showEmployee("Ben" , 12000)
showEmployee("Jessa")

def outter_Func(a,b):
    
    def sum(a,b):
       return a + b
    add = sum(a,b)
    return add+5


re = outter_Func(5,10)
print(re)
def add(num):
    if num:
        return num + add(num-1)  we want : 10 + 9 + ...
    else:                       formula : num + add(num-1) because we want recursive 
        return 0
re = add(10)
print(re)
""" 

"""
def display_Student(name,age):
    print(name,age)

display_Student("Emma" , 16)

show_student = display_Student
show_student("Emma" , 16)
"""
print(list(range(4,30,2)))

