##Полімофізм
#class Animal:
#    def sound(self):
#        pass #пустий кож
#class Dog(Animal):
#    def sound(self):
#        return "ГАВ"
#class Cat(Animal):
#    def sound(self):
#        return "МЯУ"
#class Cow(Animal):
#    def sound(self):
#        return "МУ"
#
#def speak(an):
#    print(an.sound())
#a1=Dog()
#a2=Cat()
#a3=Cow()
#speak(a1)
#speak(a2)
#speak(a3)
#
##Дозволяє використовувати один інтерфейс, але по різному
from tkinter.font import names


#class Pay:
#    def process(self,money):
#        pass
#class Credit(Pay):
#    def process(self,money):
#        return "Оплата "+str(money)+ "грн здійснена через кредитну картку."
#class Cash(Pay):
#    def process(self,money):
#        return "Оплата " +str(money)+ "грн здійснена через готівку."
#class System(Pay):
#    def process(self,money):
#        return "Оплата " +str(money)+ "грн здійснена через онлайн систему."
#buy=[Credit(),Cash(),System()]
#num=int(input('Введіть суму покупки: '))
#for k in buy:
#    print(k.process(num))



##Інкапсуляція
##модифікація доступу
##public
#class Dog:
#    def __init__(self,name):
#        self.name=name
#dog1=Dog('Бані')
#print(dog1.name)
#
##private
#class Dog:
#    def __init__(self,name):
#        self.name=name
#        self.__age=2
#    def info(self):
#        return self.__age
#dog1=Dog('Бані')
#print(dog1.info())
#
##protected
#class Dog:
#    def __init__(self,name):
#        self.name=name
#        self._bread="бульдог"
#class D (Dog):
#    def info(self):
#        return "Це щеня породи "+self._bread
#dog1=D('Бані')
#print(dog1.info())



#class Person:
#    def __init__(self,name,age,salary):
#        self.name=name #публічний атрибут
#        self._age=age #захищений
#        self.__salary=salary #приватний
#    def info(self):
#        print("Вітаю. Мене звати",self.name)
#        self._infoAge()
#        self.__infoSalary()
#    def _infoAge(self):
#        print('Мій вік',self._age)
#    def __infoSalary(self):
#        print('Мій ЗП',self.__salary)
#class Employee(Person):
#    def __init__(self, name, age, salary,pos):
#        super().__init__(name,age,salary)
#        self.pos=pos
#    def printInfo(self):
#        print('Моя посада',self.pos)
#        print('Мій вік',self._age)
#        #print('Моя Зп',self.__salary) #помилка у доступі захищенності
#human=Person('Олеся', 20, 2000)
#emp=Employee('Петро', 25, 45000, 'інженер')
#print(human.name)
#human.info()
#print(' ')
#print(emp.name)
#emp.printInfo()
#print(emp._age)
#print(emp._Person__salary)
