print("(Спочатку привітайтеся)")
import random
while True:
    user = input("You: ")
    user = user.lower()

    if user in ("hello", "hi", "привіт"):
        print("Привіт ヾ(^▽^*)))")
    elif user == "Бувай":
        print("Бувай! До зустрічі!")
        break
    elif user in "як ти?":
        print("Нерогано ~(￣▽￣)~*")
#Ще п'ять фраз
    elif user in "як тебе звуть?":
        print("Не знаю （；´д｀）ゞ")
    elif user in "слава україні!":
        print("Героям слава!ヾ(≧▽≦*)o")
    elif user in ("який твій улюблений колір?"):
        responses = ("Червоний", "Помаранчевий", "Жовтий", "Зелений", "Блакитний", "Синій", "Фіолетовий", "Чорний", "Білий", "Коричневий")
        print(random.choice(responses))
    elif user in "що ти їв сьогодні на сніданок?":
        print("НЕ СКАЖУ! (oﾟvﾟ)ノ")
    elif user in "скільки грошей на рахунку?":
        print("Багато o(*￣▽￣*)o")