def multi_or_sum(num1, num2):
    product = num1 * num2 
    sum = num1 + num2 

    if product <= 1000:
        return product
    else :
        return sum  
    
#first condition
result = multi_or_sum(20, 30)
print("The result is", result)
#Second condition 
result = multi_or_sum(30,40)
print("The result is" , result)

#Ex2
pre_num = 0
for i in range(0,10):

    sum  = i + pre_num  
    print("current number:" , i, "Previous Number:" ,pre_num, "sum= ", sum)
    pre_num = i


