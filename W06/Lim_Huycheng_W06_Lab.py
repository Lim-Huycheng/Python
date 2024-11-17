#excercise 1 
print("Excercise 1")
class User:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
    def get_username(self):
        print(f"Username: {self.__username}")
    def verify_password(self,user_password):
        if self.__password == user_password:
            print(f"Password Verified:{True}")
        else:
            print(f"Password Verified:{False}")

get_user = User("Cyber_user" , "123")
get_user.get_username()
get_user.verify_password("123")
get_user.verify_password("12345")
print("\n")

#excercise 2 
print("Excercise 2")
class UserProfile:
    def __init__(self,username,phone_number):
        self.__username = username
        self.__phone_number = phone_number
    def display_public_info(self):
        print(f"Username: {self.__username} , Phone: XXX-XXX-{self.__phone_number[-4:]}")
        # print(f"Phone: XXX-XXX-{self.__phone_number[-4:]}")
    def update_phone_number(self,old_phone_number , new_phone_number):
        if old_phone_number == self.__phone_number:
            self.__phone_number = new_phone_number
            print("Contact info updated successfully.")
            # print(f"Username: {self.__username}, Phone: {new_phone_number}")
        
user_name = UserProfile("Cyber_user" ,"012-345-6789")
user_name.display_public_info()
user_name.update_phone_number( "012-345-6789", "096-992-2799")
user_name.display_public_info()
print("\n")

#excercise 3
print("excercise 3")
class Malware:
    def describe(self):
        return "This is a malware."
class Ransomware(Malware):
    def encrypt_files(self):
        return "Files are begin encrypted."

obj_ransomeware = Ransomware()
print(f"Malware Description: {obj_ransomeware.describe()}")
print(f"Ransoware Desciprtion: {obj_ransomeware.describe()}")
print(f"Ransomware Action: {obj_ransomeware.encrypt_files()}")

#exercise 4
print("Excercise 4\n")
class Virus(Malware):
    def replicate(self):
        return "Virus is replicating."
class Trojan(Malware):
    def hide_in_files(self):
        return "Hiding in files."
class KeyLogger(Trojan):
    def describe(self):
        return "This is a keylogger. Capturing keystrokes"

obj_virus = Virus()
obj_trojan = Trojan()
obj_keylogger = KeyLogger()
print(f"Virus Description: {obj_virus.describe()}")
print(f"Virus Action: {obj_virus.replicate()}")
print(f"Trojan Description: {obj_trojan.describe()}")
print(f"Trojan Action: {obj_trojan.hide_in_files()}")
print(f"Keylogger Description: {obj_keylogger.describe()}")
print(f"Leylogger Action: {obj_keylogger.hide_in_files()}\n")

# excercise 5 
print("excercise 5\n")
class Logger:
    def log(self, massage=0, error_code=0, details=0):
        if massage !=0:
            print(f"Log: {massage}")
        elif error_code and details !=0:
            print(f"Error code: {error_code}, Detail: {details}")
        elif error_code == 200:
            print(f"Error code: {error_code}, Detail: OK")
        else:
            print("Unknown log format")
loger=Logger()
loger.log("System started")
loger.log(error_code=400, details={"url:" "not found"})
loger.log()

# excercise 6
print("\nExcercise 6")
class FirewallRule:
    def apply_rule(self):
        return "Applying generic rule."
class IPBlockRule(FirewallRule):
    def apply_rule(self):
        return "Blocking IP address."
class PortBlockRule(FirewallRule):
    def apply_rule(self):
       return "Blocking port number."

def firewall_obj(objs):
    for obj in objs:
        print(f"Firewall Action: {obj.apply_rule()}")

fire = FirewallRule()
ip = IPBlockRule()
port = PortBlockRule()
firewallRule= [fire, ip, port]
firewall_obj(firewallRule)







