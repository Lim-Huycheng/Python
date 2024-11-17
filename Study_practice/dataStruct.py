#excercise 1
print("ex1")
list1 = [100,200,300,400,500]  
list1.reverse()
print(list1)

#excercise 2
print("ex2")
li1 = ["M" , "na" , "i" , "ke"]
li2 = ["y" , "me" , "s" , "lly"]
list3 = [i + j for i , j in zip(li1,li2)]
print(list3)

#excercise 3
print("ex3")
numbers = [1,2,3,4,5,6,7]
re = [i**2 for i in numbers]
print(re)

#excercise 4
print("ex4")
l1 = ["hello" , "take"]
l2 = ["dear" , "sir"]
res = [i + j for i in l1 for j in l2]
print(res)

#excercise 5
print("ex5")
rang1 = [10,20,30,40]
rang2 = [100,200,300,400]

for x ,y in zip(rang1,rang2[::-1]):
    print(x,y)

#excercise 6
print("ex6")
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))#list() is another function to create a new list which have alreay exited
print(res)

# excercise 7 using nested list 
print("ex7")
ori_list = [10 , 20 , [300 ,400 , [5000 , 6000] , 500], 30 , 40]
ori_list[2][2].append(7000)
print(ori_list)

# excercise 8
print("ex8")
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

# excercise 9
print("EX9")
list9 = [5,10,15,20,25,50,20]
index = list9.index(20) #index = 20
list9 [index] = 200 #change element 20 to 200
print(list9)

# exercise 10 removes all 20 element
print("Ex10")
print("excercise10")
list10 = [5,20,15,20,25,50,20]
for i in list10:
    if 20 in list10:
        list10.remove(20)
print(list10)

# solution2
# while 20 in list10:
#     list10.remove(20)
# print(list10)
