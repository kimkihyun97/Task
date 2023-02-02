#10.9
class Bear():
    def eat(self):
        return "berries"

class Rabbit() :
    def eat(self):
        return "clover"

class Octothorpe():
    def eat(self):
        return "campers"

Bear = Bear()
Rabbit = Rabbit()
Octothorpe = Octothorpe()

print(Bear.eat())
print(Rabbit.eat())
print(Octothorpe.eat())

#10.10
class Laser():
    def does(self):
        print("disintegrate")
        super().does()


class Claw() :
    def does(self):
        print("crush")
        super().does()


class Smartphone():
    def does(self):
        print('ring')



class Robot(Laser,Claw,Smartphone):
    def does(self):
        super().does()





Inha =Robot()

print(Inha.does())



