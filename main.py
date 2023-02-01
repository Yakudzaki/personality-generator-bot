import aiogram
import logging
import faker
from faker import Faker
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.types import ParseMode, Message
from keyboard import *



logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer('''Здраствуйте, я генератор рандомной личности.
Если вам нужно сгенерировать личность, нажмите на данную кнопку:''', reply_markup=start_menu())



@dp.message_handler(text = 'Сгенерировать рандомную личность')
async def gen_kb(message: types.Message, state: FSMContext):
    fake = Faker()
    faker_ru = Faker('ru_RU')
    faker_name = faker_ru.name()
    faker_adress = faker_ru.address()
    faker_city = faker_ru.city()
    faker_email = faker_ru.email()
    faker_password = faker_ru.password()
    fake_phone_number = faker_ru.phone_number()
    fake_credit_card_number = faker_ru.credit_card_number()
    fake_credit_card_expire = faker_ru.credit_card_expire()
    fake_credit_card_security_code = faker_ru.credit_card_security_code()
    await message.answer(text = f'''Ф.И.О: {faker_name}
---
Город: {faker_city}
---
Адрес: {faker_adress}
---
Номер телефона: {fake_phone_number}
---
Карта: {fake_credit_card_number}, {fake_credit_card_expire}, {fake_credit_card_security_code}
---
Почта: {faker_email}
Пароль: {faker_password}\n\nDeveloper - @Yakudza_Drill
''', reply_markup=start_menu())

if __name__ == "__main__":
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)