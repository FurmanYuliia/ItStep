import requests
import tkinter as tk

URL1 = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
URL2 = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&json"

response = requests.get(URL1)
rate = response.json()
dollar = rate[0]["rate"]

response = requests.get(URL2)
rate = response.json()
euro = rate[0]["rate"]

def change_rate(currency):
    global dollar
    if currency == "USD":
        price1.config(text=f"{round(8000 / dollar, 2)} USD")
    elif currency == "UAH":
        price1.config(text="8000 UAH")
    elif currency == "EUR":
        price1.config(text=f"{round(8000 / euro, 2)} EUR")

root = tk.Tk()
root.geometry("400x400")

tk.Button(root, text="UAH", command=lambda: change_rate("UAH")).pack(anchor="w", padx=10)
tk.Button(root, text="USD", command=lambda: change_rate("USD")).pack(anchor="w", padx=10)
tk.Button(root, text="EUR", command=lambda: change_rate("EUR")).pack(anchor="w", padx=10)


tk.Label(root, text="Phone").pack(anchor="w", padx=10)
price1 = tk.Label(root, text="8000 UAH")
price1.pack(anchor="w", padx=10)

root.mainloop()


