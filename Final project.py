import requests
from bs4 import BeautifulSoup as bs

class ALLO:
    def __init__(self,url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            print("Не вдалося підключитися до сайту")
    def getInfo(self):
        telephone=[]
        tel = self.soup.find_all('div', class_='page__content')
        if not tel:
            print('Помилка в пошуку на сторінці')
            return telephone
        for i in tel[0:10]:
            name=i.find('a', class_='product-card__title')
            nameErorr=name.text.strip() if name else 'Відсутня назва'
            price=i.find('div', class_='v-pb__cur discount')
            priceErorr=price.text.strip() if price else 'Відсутня ціна'
            telephone.append(
                {
                    'Назва':nameErorr,
                    'Ціна':priceErorr,
                }
            )
        return telephone
    def showInfo(self,telephone):
        print('№\t','НАЗВА','\t'*4,'ЦІНА','\t'*4)
        print('-' * 80)
        for i in telephone:
            print('\t',i['Назва'],'\t',i['Ціна'])
url='https://allo.ua/ua/products/mobile/proizvoditel-apple/'
obj=ALLO(url)
obj.auditSite()
telephone=obj.getInfo()
print('\t10 телефонів від Apple\n')
if telephone:
    obj.showInfo(telephone)
else:
    print("Жодної інформації не отримано")