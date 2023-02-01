from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def start_menu():
    start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    generator_kb = KeyboardButton("Сгенерировать рандомную личность")
    start_kb.add(generator_kb)

    return start_kb