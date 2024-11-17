class Duck:
    def sound(self):
        return "Quack!!!"
class Human:
    def sound(self):
        return "Annyeong!!!"
def makesound(obj):
    print(obj.sound())
d = Duck()
h = Human()
makesound(d)
makesound(h)


class Vehicle:
    def speed(self):
        print("fast , slow")
class Car(Vehicle):
    def speed(self):
        print("This car is soo fast!!!")

vehicle = Vehicle()
vehicle.speed()
vehicle = Car()
vehicle.speed()


class kpop:
    def __init__(self,group):
        self.group = group
    def bias(self):
        print("Winter,Jay,Yeji,Jaehyun,Mark Lee,Ruka")
my_kpop = kpop("Enhypen")
print(hasattr(my_kpop,"bias")) #Checking for Function. #Output: True
print(hasattr(my_kpop,"Doeun"))#Output: False
print(hasattr(my_kpop,"group"))#Checking for attributes.#Output: True


