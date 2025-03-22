#Зв'язок класів
#class Human:
#    count=0
#    def __init__(self,name="Vasya"):
#        self.name=name
#        Human.count+=1
#class Auto:
#    def __init__(self,brand):
#        self.brand=brand
#        self.passenger=[]
#    def add(self,*args): #Необмежена кількість пасажирів
#        for n in args:
#            self.passenger.append(n)
#    def info(self):
#        if self.passenger==[]:
#            print('Пасажири відсутні у ',self.brand)
#        else:
#            print('Пасажири присутні у ',self.brand,": ")
#            for n in self.passenger:
#                print(n.name)

#pas1=Human()
#pas2=Human('Таня')
#pas3=Human('Саша')
#car1=Auto('Богдан')
##car1.add(pas1)
##car1.info()
#car1.add(pas1,pas2,pas3)
#car1.info()
#print(Human.count)

########

#class Human: #Загальний шаблон
#    def __init__(self,name,age,height,city,animal):
#        self.name=name
#        self.age=age
#        self.height=height
#        self.city=city
#        self.animal=animal
#    def __str__(self):
#        return 'Вітаю! Я ' + self.name+ '. Мені ' +str(self.age)+' років. Я з міста ' +self.city+'. Мій зріст ' +str(self.height)+ '. Наявність тварин:'+ self.animal +'.'#Такий метот виводе лише текст
#
#class Pupil(Human):
#    def __init__(self,name,age,height,city,animal,school,clas):
#        super().__init__(name,age,height,city,animal)
#        self.school=school
#        self.clas=clas
#    def __str__(self):
#        return super().__str__()+' Навчаюсь у школі '+str(self.school) +' у '+str(self.clas)+' класі'
#
#class Worker(Human):
#    def __init__(self,name,age,height,city,animal,job,salary):
#        super().__init__(name,age,height,city,animal)
#        self.job=job
#        self.salary=salary
#    def __str__(self):
#        return super().__str__()+' Працюю на посаді '+self.job+', маю зп '+ str(self.salary)+'$'
#
#h=Human('Маша',12, 156,'Запоріжжя','кіт')
#p=Pupil('Олег', 14, 170, 'Дніпро', "папуга", 101, 9)
#w=Worker('Яна', 35, 168, 'Львів', 'немає', 'дизайнер', 3500)
#print(str(h))
#print(p.__str__()) #або print(str(p)) або print(p)
#print(w)


class PC:
    def __init__(self,model="HP"):
        super().__init__()
        self.model=model
        self.memory=256
class Display:
    def __init__(self):
        super().__init__()
        self.res='4k'
class Smart(PC,Display):
    def info(self):
        print('Смартфон моделі',self.model,"має об'єм пам'яти",self.memory,"Мб та розширення екрана", self.res)

tel=Smart('Samsung')
tel.info()