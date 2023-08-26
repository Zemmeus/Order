#pip install -r req.txt
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from aiogram.types import Message, MediaGroup
from aiogram.types import InputMediaDocument
from states import Form
import pygsheets

path='studious-rhythm-390907-798ae3194f44.json'
gc = pygsheets.authorize(service_account_file=path)
sh = gc.open('pythontest')
wks = sh[0]
bot = Bot(token='6337739495:AAE7Qveg0EY9__5gyFQuIERakbbJfZUkW5U')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

data = []


Estimilated_UK_sizes = {
    0: "AA",
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "DD",
    6: "E",
    7: "F",
    8: "FF",
    9: "G",
    10: "GG",
    11: "H",
    12: "HH",
    13: "J",
    14: "JJ",
    15: "K",
    16: "KK",
    17: "L",
    18: "LL",
    19: "M",
    20: "MM",
    21: "N",
    24: "OO",
}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Запустить")
    keyboard.add(button_1)
    await message.answer("Добро пожаловать на онлайн \n Я виртуальный помощник  от  \n Жми «запустить» и мы начнем", reply_markup=keyboard)
    await Form.name1.set()

@dp.message_handler(commands=['restart'])
async def restart(message: types.Message):
    await message.answer("Вы перезапустили бота")
    await message.answer("Как я могу к тебе обращаться?")
    await Form.name1.set()


@dp.message_handler(lambda message: message.text == "Запустить", state=Form.name1)
async def process_start(message: types.Message, state: FSMContext):
    await message.answer("Как я могу к тебе обращаться?")
    await Form.name2.set()


@dp.message_handler(state=Form.name2)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer(f"Отлично, {message.text}, подскажи пожалуйста, сколько тебе лет?")
    await Form.diff.set()


@dp.message_handler(state=Form.diff)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    if data["age"].isdigit():
        await message.answer(f"Расскажи пожалуйста, с какими трудностями ты сталкиваешься при подборе? ")
        await Form.age.set()
    else:
        await message.answer('Введи целое положительное число')        

@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['diff'] = message.text
    photo=open('test.png','rb')
    if data['age'].isdigit():
        await message.answer(f"Спасибо, что поделилась ❤️, мы обязательно решим твою проблему. Ты уже на первом шагу к своему идеальному______. Выбери свой тип Ф___ и напиши ответ цифрой (от 1-6)")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await Form.F.set()
    else:
        await message.answer('Введи целое положительное число')


@dp.message_handler(state=Form.F)
async def process_f(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['f'] = message.text
    photo=open('test.png','rb')
    if data['f'].isdigit() and 1 <= int(data['f']) <= 6:
        await message.answer(f"Превосходно! Давай перейдем к твоей ____ выбери свою форму___(от 1-12)")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await Form.Position.set()
    else:
        await message.answer('Введи число от 1 до 6')


@dp.message_handler(state=Form.Position)
async def process_position(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Forma'] = message.text
    photo=open('test.png','rb')
    if data['Forma'].isdigit() and 1 <= int(data['Forma']) <= 12:
        await message.answer(f"Выбери расположение……..\n(Фото с выбором 1 или 2)")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await Form.OPGinhale.set()
    else:
        await message.answer('введи число от 1 до 12')


@dp.message_handler(state=Form.OPGinhale)
async def process_OPGinhale(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Position'] = message.text
    if data['Position'].isdigit() and 1 <= int(data['Position']) <= 2:
        await message.answer("Супер! До консультации и подарочной скидки 20% на остался последний шаг")
        await message.answer("Сделай замеры ОПГ вдох")
        await Form.OPGouthale.set()
    else:
        await message.answer('введи число от 1 до 2')       


@dp.message_handler(state=Form.OPGouthale)
async def process_OPGouthale(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['OPGinhale'] = message.text
    if data['OPGinhale'].isdigit() and 50 <= int(data['OPGinhale']) <= 150:
        await message.answer("Сделай замеры ОПГ выдох")
        await Form.OG.set()
    else:
        await message.answer('Введи целое положительное число')


@dp.message_handler(state=Form.OG)
async def process_OG(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['OPGouthale'] = message.text
    if data['OPGouthale'].isdigit() and 50 <= int(data['OPGouthale']) <= 150:
        await message.answer("Сделай замеры ОГ")
        await Form.size.set()
    else:
        await message.answer('Введи целое положительное число')

@dp.message_handler(state=Form.size)
async def process_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['OG'] = message.text

    if data['OG'].isdigit() and 50 <= int(data['OG']) <= 150:
        await message.answer(" Мы уже определили твой размер___! Осталось узнать твой размер____ ")
        await Form.pdf1.set()
    else:
        await message.answer('Введи целое положительное число')

@dp.message_handler(state=Form.pdf1)
async def process_pdf1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    if data['size'].isdigit() and data["f"] in ["1", "2", "3", "4", "5"] and data["Forma"]=="12" and data["Position"] in ["1", "2"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set()
    elif data['size'].isdigit() and data["f"] in ["6"] and data["Forma"] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"] and data["Position"] in ["1", "2"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set()
    elif data['size'].isdigit() and data["f"] in ["1", "2", "3", "4", "5"] and data["Forma"] in ["1"] and data["Position"] in ["1", "2"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set() 
    elif data['size'].isdigit() and data["f"] in ["1", "2", "3", "4", "5"] and data["Forma"] in ["2", "3", "4", "5", "9", "10", "11"] and data["Position"] in ["1"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set() 
    elif data['size'].isdigit() and data["f"] in ["1", "2", "3", "4", "5"] and data["Forma"] in ["2", "3", "4", "5", "9", "10", "11"] and data["Position"] in ["2"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set()
    elif data['size'].isdigit() and data["f"] in ["1", "2", "3", "4", "5"] and data["Forma"] in ["8"] and data["Position"] in ["1"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set()    
    elif data['size'].isdigit() and data["f"] in ["1", "2", "3", "4", "5"] and data["Forma"] in ["8"] and data["Position"] in ["2"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set()    
    elif data['size'].isdigit() and data["f"] in ["1", "2", "3", "4", "5"] and data["Forma"] in ["7"] and data["Position"] in ["1", "2"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set()     
    elif data['size'].isdigit() and data["f"] in ["1", "2", "3", "4", "5"] and data["Forma"] in ["6"] and data["Position"] in ["1", "2"]:
        await message.answer_document(open("asd.pdf", "rb"))
        await message.answer("Благодарим тебя за ответы о твоих особенностях ___. Высылаем каталог нашего ассортимента, подходящего именно тебе. Тебе осталось всего лишь выбрать ___ по твоим предпочтениям и вкусу. Напиши код поправившего товара и цвет через запятую для твоей примерки с ____(пдф файлы по цифрам)")
        await Form.address.set()              
    else:
        await message.answer('Введи целое положительное число')

@dp.message_handler(state=Form.address)
async def process_pdf2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pdf1'] = message.text
    await message.answer("Спасибо за заказ! Надеемся, наше ____ подарит тебе незабываемый комфорт и удобство ______. Пожалуйста, напиши свой полный адрес. Напоминаем, что оплата за товар производится после примерки и ______консультации. ")
    await Form.number.set()

@dp.message_handler(state=Form.number)
async def process_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer("Мы хотели бы убедиться, что заказ оформлен правильно и все твои пожелания учтены. Пожалуйста, напиши свой контактный номер телефона")
    await Form.end.set()

@dp.message_handler(state=Form.end)
async def process_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
    if data['number'].isdigit():
        await message.answer("Превосходно! Мы свяжемся с тобой в ближайшее время. Благодарим за твой выбор Bra Studio")
        await message.answer("Напишите 'Да' если хотите перезапустить бота")
        await Form.end2.set()
        async with state.proxy() as data:
            FirstFormula = int(data['OPGinhale']) - 8
            SecondFormula = (int(data['OG']) - int(data['OPGinhale'])) / 2.54
            SecondFormula = int(SecondFormula)
            print(FirstFormula, SecondFormula)
            if SecondFormula in Estimilated_UK_sizes:
                size = Estimilated_UK_sizes[SecondFormula]
                data["Formula"] = (str(FirstFormula) + size)
            else: 
                data['Formula'] = "Данные не подходят под таблицу"

            data["ID"] = message.from_user.id
            data["UserName"] = message.from_user.full_name

            print(data)

            x = [[i for i in data.values()]]

            wks.append_table(x, start='A2', end=None,
                            dimension='ROWS', overwrite=False)
        await message.answer(data)
    else:
        await message.answer('Введи целое положительное число')

@dp.message_handler(state=Form.end2)
async def processend2(message: types.Message, state: FSMContext):
    await message.answer("Как к тебе обращаться?")
    await Form.name2.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# @dp.message_handler(state=Form.end)
# async def process_size(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['number'] = message.text
#     if data['number'].isdigit():
#         await message.answer("Превосходно! Мы свяжемся с тобой в ближайшее время. Благодарим за твой выбор Bra Studio")
#         await Form.pdf1.set()
#     else:
#         await message.answer('Введи целое положительное число')

