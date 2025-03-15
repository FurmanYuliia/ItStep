class Car:
    #speed=110
    def __init__(self,speed):
        self.speed=speed
    def info(self):
        print("Швидкість авто: ",self.speed)
sp=int(input('Максимальна шв авто: '))
auto=Car(sp)
#print("Швидкість авто:",auto.speed)
auto.info()
auto2=Car(180)
auto2.info()