from aiogram import types

def category_kb():
    keyboard = types.ReplyKeyboardMarkup(
        keyboard = [
            [types.KeyboardButton(text='Sedan')],
            [types.KeyboardButton(text='SUV'),
            types.KeyboardButton(text='Van')],
            [types.KeyboardButton(text='Hatchback')]
        ],
        resize_keyboard=True
    )
    return keyboard