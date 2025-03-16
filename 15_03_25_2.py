#Симулятор студента
import random as r
class Student:
    def __init__(self,name):
        self.name=name
        self.happy=r.randint(10, 100)
        self.progress=r.randint(0, 10)
        self.money=r.randint(-50, 100)
        self.alive=True
    def study(self):
        print('Час для навчання')
        self.happy-=r.randint(1, 50)
        self.progress+=r.randint(1, 7)
    def sleep(self):
        print('Час для сну')
        self.happy += r.randint(1, 50)
    def chill(self):
        print('Час для відпочинку')
        self.happy+=r.randint(1, 20)
        self.progress-=r.randint(5, 10)
    def earnings(self):
        print('Час для заробітку')
        self.happy += r.randint(1, 5)
        self.money += r.randint(100, 200)
    def expenses(self):
        print('Трата грошей')
        self.happy += r.randint(10, 90)
        self.money -= r.randint(10, 200)
    def isAlive(self):
        if 1<self.progress<5:
            print('Ти на грані відрахування. Починай навчатися')
            self.alive = False
        elif self.progress <=1:
            print('Відрахування з інституту')
            self.alive = False
        elif self.progress >= 5:
            print('Відмінно навчаєшся')
            self.alive = True
        elif self.earnings <= 10:
            print('Треба піти на роботу!')
            self.alive = False
        elif self.expenses >=200:
            print('Витрачай гроші розумніше')
            self.alive = True
    def everyday(self):
        print("Рівень щастя", self.happy)
        print("Гроші", self.money)
        print("Прогрес навчання", self.progress)
    def studyLife(self,day):
        day="\nДень №"+str(day)
        print(day)
        res=r.randint(1, 3)
        if res==1:
            self.study()
        elif res==2:
            self.chill()
            self.expenses()
            self.earnings()
        else:
            self.sleep()
        self.everyday()
        self.isAlive()

st1=Student('Олег')
#print(st1.progress)
print("Життя студента", st1.name)
for k in range(1,8):
    if st1.alive==False:
        break
    st1.studyLife(k)
