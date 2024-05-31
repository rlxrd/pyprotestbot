from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

import keyboards as kb

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в интернет магазин кроссовок!', reply_markup=kb.main)


@user.callback_query(F.data == 'back')
@user.message(F.text == 'Каталог')
async def catalog(message: Message | CallbackQuery):
    if isinstance(message, Message):
        await message.answer('Это каталог товаров. Выберите интересующий товар.', reply_markup=await kb.catalog())
    else:
        await message.message.delete()
        await message.answer('Вы вернулись назад')
        await message.message.answer('Это каталог товаров. Выберите интересующий товар.', reply_markup=await kb.catalog())


@user.callback_query(F.data.startswith('sneakers_'))
async def adidas(callback: CallbackQuery):
    await callback.answer('Вы выбрали товар')
    await callback.message.delete()
    await callback.message.answer_photo(photo='https://sneakerbardetroit.com/wp-content/uploads/2021/08/adidas-Yeezy-Boost-350-V2-MX-Oat-GW3773-2021-Release-Date.jpg',
                                        caption=f'Товар: {callback.data.split('_')[1]}\nЦена: приемлемая',
                                        reply_markup=kb.back)
