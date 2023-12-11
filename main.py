#TG bot
import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from aiogram.filters import Command
import logging
import random
from pathlib import Path

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


images_directory = Path('/Users/bektur/Downloads/cars sample')


@dp.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    ca = []
    p = Path('/Users/bektur/Downloads/cars sample')
    for c in p.iterdir():
        ca.append(c)
    file = types.FSInputFile(random.choice(ca))
    await message.answer_photo(
        photo=file,
    )

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}')

@dp.message()
async  def echo(message: types.Message):
    await message.reply(
        f'{message.text}, {message.from_user.first_name}, {message.from_user.username}'
    )

async def main():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='начало'),
        types.BotCommand(command='random_pic', description='случайная картинка')
    ])
    #обрабатываем все сообщения
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    #запускаем бота
    asyncio.run(main())