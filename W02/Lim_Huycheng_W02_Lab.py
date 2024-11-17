# excercise 1
print("Exercise1")
def reverse_list(input_list):
    return list(input_list[::-1])
input_list = [1,2,3,4,5]
print("input: ",input_list)
reversed_list = reverse_list(input_list)
print("Output: " ,reversed_list)

# excercise 2
print("Excercise 2")
list = []
[list.append(n**2) for n in range(1,21) if n%2 == 0]
print("Output:",list)

# excercise 3
print("Excercise 3")
def merge_list(list1,list2):
    marged_list = list1 + list2
    print(marged_list)
    new_list = []
    for i in marged_list:
        if i  in new_list:
            continue
        else :
            new_list.append(i)
    return new_list

list1 = [1,2,3] 
list2 = [2,3,4,5]
result = merge_list(list1,list2)
print("Output:" ,result)   

#excercise 4
print("excercise 4")
def max_min(tuple1):
    max_value = max(tuple1)
    min_value = min(tuple1)
    return (max_value , min_value)

tuple1 = (10,5,8,12,3)
out = max_min(tuple1)
print("Output:" , out)   

# excercise 5 
print("Excercise 5")
def display_information(infor):
    for city, latitude, longitude in infor:
        print("City: {}, Latitude: {}, Longitude: {}".format(city, latitude, longitude))
infor= (
    ("Phnom Penh", 11.5564, 104.9282),
    ("Siem Reap", 13.3622, 103.8597),
    ("Battambang", 13.0957, 103.2022)
)
display_information(infor)

# excercise 6 
# syntax =  lambda arguments : expression
print("Excercise 6")
dict = {1:10 , 2: 20 ,3: 30, 4:40}
get_value =  lambda dict: {key: value *2 for key , value in dict.items()}
final_re = get_value(dict)
print("Input:" , dict)
print("Output: " , final_re) 

# excercise 7
print("Excercise 7")
def frequency_list(take_input):
    new_frequency = {}
    for word in take_input:
        if word in new_frequency:
            new_frequency[word]+= 1
        else:
            new_frequency[word]= 1
    return new_frequency
        
input_string = "hello"
print("Input:",input_string)
take_input = frequency_list(input_string)
print("Output: ", take_input)

# excercise 8
print("Excercise 8")
def re_value(dictionary1,dictionary2):
    for k , v in dictionary2.items():
        if k in dictionary1:
            dictionary1[k] += v
        else:
            dictionary1[k] = v
    return dictionary1

dictionary1 = {"a" : 1 , "b": 2} 
dictionary2 = {"b": 3, "c":4 }
print("Input: " , dictionary1 , dictionary2)
output = re_value(dictionary1,dictionary2)
print("Output:" , output)

#Bonus 
print("Bonus excercise")

def add_user(users, username, email, status):
    users.append({"username": username, "email": email, "status": status})
    print(f"User '{username}' added successfully.")
    # print(users)
def remove_user(users, username):
    for user in users:
        if user["username"] == username:
            users.remove(user)
            print("User '{}' removed successfully.".format(username))
            break
    # print(users)
           
def update_user_status(users, username , new_status):
    for user in users:
        if user["username"] == username:
            user["status"] = new_status
            print("User '{}' status updated to '{}'".format(username,new_status))
            break
        
def display_users(users):
    print("Current user account")
    print("Username             Email               Status")
    print("-" * 60)
    for user in users:
        print(f"{user['username']:<15} {user['email']:<25} {user['status']}")

def count_active_users(users):
   return sum(1 for user in users if user['status'] == "active")

users = [
 {"username": "alice", "email": "alice@example.com", "status": "active"},
 {"username": "bob", "email": "bob@example.com", "status": "suspended"},
 {"username": "charlie", "email": "charlie@example.com", "status": "active"}
]

add_user (users , "dave", "dave@example.com", "active")
remove_user(users, "bob")
update_user_status(users, "charlie", "suspended")
display_users(users)
print("Active users:", count_active_users(users))



        



