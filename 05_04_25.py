#1
import requests #запит
from bs4 import BeautifulSoup as bs
class Books:
    def __init__(self,url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response= requests.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text,"html.parser")
        else:
            print("Не вдалося підключитися до сайту")
            return
    def getInfo(self):
        book=[]
        bo=self.soup.find_all('div',class_='page_inner')
        if not bo:
            print('Помилка в пошуку на сторінці')
            return book
        for i in bo[0:8]:
            name=i.find('a',class_='catalogue/a-light-in-the-attic 1000/index.html')
            nameErorr=name.text.strip() if name else 'Відсутня назва'
            #if name:
            #    name.text()
            #else:
            #    print('Відсутня назва')
            price=i.find('p',class_='price_color')
            priceErorr = price.text.strip() if price else 'Відсутня ціна'
            stars = i.find('p', class_='star-rating Three')
            starsErorr = stars.text.strip() if stars else 'Відсутні зірки'
            book.append(
                {
                    'Назва':nameErorr,
                    'Ціна':priceErorr,
                    'Зірки':starsErorr,
                }
            )
        return book
    def showInfo(self,book):
        print('№\t','НАЗВА','\t'*2,'ЦІНА','\t'*2,'ЗІРКИ','\t'*2)
        print('-'*50)
        for i in book:
            print('\t',i['Назва'],'\t',i['Ціна'],'\t',i['Зірки'])
url='http://books.toscrape.com'
obj=Books(url)
obj.auditSite()
book=obj.getInfo()
print('\tНайпопулярніші 8 книг\n')
if book:
    obj.showInfo(book)
else:
    print("Жодної інформації не отримано")

print(' ')
print(' ')
print(' ')

#2
import requests #запит
from bs4 import BeautifulSoup as bs

class Metro:
    def __init__(self,url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response= requests.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text,"html.parser")
        else:
            print("Не вдалося підключитися до сайту")
            return
    def getInfo(self):
        knife=[]
        k=self.soup.find_all('div',class_='Container')
        if not k:
            print('Помилка в пошуку на сторінці')
            return knife
        for i in k[0:3]:
            name=i.find('span',class_='ProductTile__title')
            nameErorr=name.text.strip() if name else 'Відсутня назва'
            #if name:
            #    name.text()
            #else:
            #    print('Відсутня назва')
            price=i.find('div',class_='ProductTile__prices')
            priceErorr = price.text.strip() if price else 'Відсутня ціна'
            knife.append(
                {
                    'Назва':nameErorr,
                    'Ціна':priceErorr,
                }
            )
        return knife
    def showInfo(self,knife):
        print('№\t','НАЗВА','\t'*2,'ЦІНА','\t'*2)
        print('-'*50)
        for i in knife:
            print('\t',i['Назва'],'\t',i['Ціна'])
url='https://metro.zakaz.ua/uk/search/?q=%D0%BD%D1%96%D0%B6'
obj=Metro(url)
obj.auditSite()
knife=obj.getInfo()
print('\t3 ножі\n')
if knife:
    obj.showInfo(knife)
else:
    print("Жодної інформації не отримано")
