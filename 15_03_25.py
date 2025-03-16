#class Car:

class Car:
    #speed=110
    def __init__(self,speed):
        self.speed=speed
    def info(self):
        print("Швидкість авто: ",self.speed)

    def __init__(self,year,make,model,speed):
        self.year=year
        self.make=make
        self.model=model
        self.speed=speed
    def __str__(self):
        print("Рік:", self.year,",Марка:", self.make,",Модель:", self.model,",Швидкість:", self.speed)
    def __bool__(self):
        return self.year!=None
    def __len__(self):
        return self.make
    def __len__(self):
        return self.model
    def __len__(self):
        return self.speed

a1=Car("2005", "Nissan", "Nissan Note", "160")
a1.__str__()

print(" ")
print(" ")



#class Employee:

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        print("Ім'я:", self.name, ",Посада:", self.position, "", self.salary)

    def get_salary_info(self):
            print("Заробітна плата", self.name, ":", self.salary)

    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.position
    def __len__(self):
        return self.salary


p1 = Employee("Оля", "Глав.лікар", "")
p1.__str__()
p1.salary = "250 тис."
p1.get_salary_info()