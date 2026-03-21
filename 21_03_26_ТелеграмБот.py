import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import BotCommand
import time


TOKEN = "8719689075:AAHpxqpfZCAHUIAHoQxJ5F8z_24UHos1LMY"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Історія
history = []

# Menu
async def main():
    # Встановлюємо список команд, які бачитиме користувач
    await bot.set_my_commands([
        BotCommand(command="start", description="Запустити бота"),
        BotCommand(command="help", description="Отримати допомогу")
    ])

    await dp.start_polling(bot)

# Додавання кнопок
def main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Хто ти?")],
            [KeyboardButton(text="Яка твоя улюблена погода?")],
        ],
        resize_keyboard=True
    )
    return keyboard

def course_menu1():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ясна"), KeyboardButton(text="Похмура"), KeyboardButton(text="Дощова")],
            [KeyboardButton(text="Сніжна"), KeyboardButton(text="Вітряна")],
            [KeyboardButton(text="Мінлива"), KeyboardButton(text="Затишна")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )
    return keyboard



def seasons_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Так"), KeyboardButton(text="Ні")]
        ],
        resize_keyboard=True
    )
    return keyboard

# Function
@dp.message(Command("start"))  # Коли користувач надішле /start
async def start_command(message: Message):
    if message.text in history:
        await message.answer("Ще раз вітаю!\n(✿◡‿◡)")
    else:
        history.append(message.text)  # Запам'ятовуємо питання
        await message.answer("Вітаю!\no(^▽^)o", reply_markup=main_menu() )

@dp.message(F.text=="Хто ти?")
async def start_command(message: Message):
    if message.text in history:
        await message.answer("Я вже відповів на це питання ^^")
    else:
        history.append(message.text)  # Запам'ятовуємо питання
        await message.answer("Я твій персональний помічник!\no((>ω< ))o")


@dp.message(F.text.in_(["Похмура", "Дощова", "Вітряна", "Мінлива"]))
async def weather_bad(message: Message):
    if message.text in history:
        await message.answer("Я вже знаю)", reply_markup=main_menu() )
    else:
        history.append(message.text)
        await message.answer("Уфф. Любиш холодну пору року?", reply_markup=seasons_menu()  )

@dp.message(F.text =="Так")
async def answer_yes(message: Message):
    history.append(message.text)
    await message.answer("А я не дуже люблю холод\n (>'-'<)", reply_markup=main_menu() )

@dp.message(F.text == "Ні")
async def answer_yes(message: Message):
    history.append(message.text)
    await message.answer("Хм.. Розумію тебе!", reply_markup=main_menu() )

@dp.message(F.text.in_(["Ясна", "Сніжна", "Затишна"]))
async def weather_good(message: Message):
    if message.text in history:
        await message.answer("Я вже знаю)", reply_markup=main_menu() )
    else:
        history.append(message.text)
        await message.answer("Чудова погода!!", reply_markup=main_menu() )


@dp.message(F.text=="Яка твоя улюблена погода?")
async def start_command(message: Message):
    if message.text in history:
        await message.answer("Ти вже питав про це :)")
        time.sleep(1)
        await message.answer("Сонечко!")
        time.sleep(0.6)
        await message.answer("А твоя?", reply_markup=course_menu1())
    else:
        history.append(message.text)
        await message.answer("Хмм...")
        time.sleep(1.1)
        await message.answer("Сонечко 🐞")
        time.sleep(1)
        await message.answer("А твоя?", reply_markup=course_menu1() )

# Кнопка Назад
@dp.message(F.text=="Назад")
async def start_command(message: Message):
    await message.answer("В головне меню!", reply_markup=main_menu() )


# Обробка тексту, який не розпізнав бот
@dp.message()
async def echo_all(message: Message):
    await message.answer("(Збііііійййй програаааамммии)\n＼（〇_ｏ）／")


# Запуск програми
async def main():
    await dp.start_polling(bot)

asyncio.run(main())
