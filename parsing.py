# #шаблон
# import requests #запит
# from bs4 import BeautifulSoup as bs
#
# class Name:
#     def __init__(self,url):
#         self.url=url
#         self.header={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#     def auditSite(self):
#         response= requests.get(self.url,headers=self.header)
#         if response.status_code==200:
#             self.soup=bs(response.text,"html.parser")
#         else:
#             print("Не вдалося підключитися до сайту")
#     def getInfo(self):
#         pass
#     def showInfo(self):
#         pass
# url='посилання'
# obj=Name(url)
# obj.auditSite()
# obj.getInfo()
# if site:
#     obj.showInfo()
# else:
#     print("Жодної інформації не отримано")
#шаблон
# import requests #запит
# from bs4 import BeautifulSoup as bs
#
# class Comfy:
#     def __init__(self,url):
#         self.url=url
#         self.header={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#     def auditSite(self):
#         response= requests.get(self.url,headers=self.header)
#         if response.status_code==200:
#             self.soup=bs(response.text,"html.parser")
#         else:
#             print("Не вдалося підключитися до сайту")
#             return
#     def getInfo(self):
#         laptop=[]
#         lap=self.soup.find_all('div',class_='products-catalog-grid products-catalog--grid-mode')
#         if not lap:
#             print('Помилка в пошуку на сторінці')
#             return laptop
#         for i in lap[0:4]:
#             name=i.find('a',class_='prdl-item__name ellipsis-2-lines')
#             nameErorr=name.text.strip() if name else 'Відсутня назва'
#             #if name:
#             #    name.text()
#             #else:
#             #    print('Відсутня назва')
#             price=i.find('dev',class_='products-list-item-price__actions-price-current')
#             priceErorr = price.text.strip() if price else 'Відсутня ціна'
#             laptop.append(
#                 {
#                     'Назва':nameErorr,
#                     'Ціна':priceErorr,
#                 }
#             )
#         return laptop
#     def showInfo(self,laptop):
#         print('№\t','НАЗВА','\t'*2,'ЦІНА','t'*2)
#         print('-'*50)
#         for i in laptop:
#             print('\t',i['Назва'],'\t',i['Ціна'])
# url='https://coinmarketcap.com/'
# obj=Comfy(url)
# obj.auditSite()
# laptop=obj.getInfo()
# print('\tНайпопулярніші 4 ноутбуки\n')
# if laptop:
#     obj.showInfo(laptop)
# else:
#     print("Жодної інформації не отримано")
import requests #запит
from bs4 import BeautifulSoup as bs

class Coin:
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
        coins=[]
        listCoin=self.soup.find('tbody')
        if not ListCoin:
            print('Помилка в пошуку на сторінці')
            return coins
        info=ListCoin.find_all('tr')
        for i in info:
            name=i.find('p',class_='coin-item-name') #sc-65e7f566-0 iPbTJf coin-item-name



    def showInfo(self,laptop):
        print('№\t','НАЗВА','\t'*2,'ЦІНА','t'*2)
        print('-'*50)
        for i in laptop:
            print('\t',i['Назва'],'\t',i['Ціна'])
url='https://coinmarketcap.com/'
obj=Coin(url)
obj.auditSite()
site=obj.getInfo()
print('\t5 найпопулярніші криптомонети\n')
if site:
    obj.showInfo(site)
else:
    print("Жодної інформації не отримано")