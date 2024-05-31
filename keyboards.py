from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты',
                                                    request_contact=True)]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

sneaker_brands = [
    "Nike",
    "Adidas",
    "Converse",
    "Vans",
    "New Balance",
    "Puma",
    "ASICS",
    "Brooks",
    "Saucony",
    "Hoka One One",
    "Merrell",
    "Under Armour",
    "Reebok",
    "On",
    "Veja"
]

async def catalog():
    keyboard = InlineKeyboardBuilder()
    for item in sneaker_brands:
        keyboard.add(InlineKeyboardButton(text=item, callback_data=f'sneakers_{item}'))
    return keyboard.adjust(2).as_markup()


back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back')]
])
