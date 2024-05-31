from aiogram import Router, F
from aiogram.filters import Command, Filter
from aiogram.types import Message

admin = Router()

ADMINS = [12, 345, 5525270361]


class Admin(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id in ADMINS


@admin.message(Admin(), Command('admin'))
async def cmd_start(message: Message):
    await message.answer('Hi')


@admin.message(F.from_user.id == 5525270361, Command('apanel'))
async def cmd_apanel(message: Message):
    await message.answer('hi')
