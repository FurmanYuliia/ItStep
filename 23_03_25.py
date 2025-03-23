class Cart:
    def __init__(self,money):
        super().__init__(name)
        self.money=money
    def info(self):
        print('Усього грошей у тебе:' +str(self.money))
    def __str__(self):
        return super().__str__() +'Усього грошей у тебе:' +str(self.money)



mo=int(input('Усього грошей у тебе: '))



class Product:
    count=0
    def __init__(self,name,price,presence):
        self.name=name
        self.price=price
        self.presence=presence
        Product.count+=1
    def __str__(self):
        print('Назва товару: ' +self.name+'. Ціна: ' +str(self.price)+ '. Наявність: ' +self.presence+ '.')

p1=Product('banana', 60, 'в наявності')
p1.__str__()
p2=Product('apple', 65, 'в наявності')
p2.__str__()
p3=Product('avocado', 66, 'немає в наявності')
p3.__str__()
p4=Product('bread', 50, 'в наявності')
p4.__str__()
p5=Product('fish', 56, 'в наявності')
p5.__str__()
p6=Product('orange', 48, 'немає в наявності')
p6.__str__()
p7=Product('raisin', 51, 'в наявності')
p7.__str__()
p8=Product('mandarin', 49, 'в наявності')
p8.__str__()
p9=Product('sausage', 56, 'в наявності')
p9.__str__()
p10=Product('cheese', 50, 'в наявності')
p10.__str__()
print("Всього товарів:",p1.count)