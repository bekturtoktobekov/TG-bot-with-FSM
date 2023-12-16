#TG bot
import asyncio
from aiogram import types
import logging
from pathlib import Path
from bot import bot, dp
from handlers.picture import pic_router
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.categories import categories_router
# from handlers.free_lesson import free_lesson_form_router
images_directory = Path('/Users/bektur/Downloads/cars sample')

async def main():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='начало'),
        types.BotCommand(command='random_pic', description='случайная картинка'),
        types.BotCommand(command='categories', description='модель авто'),
        # types.BotCommand(command='free lesson', description= 'Записаться на открытый урок')
    ])

    dp.include_router(pic_router)
    dp.include_router(categories_router)
    dp.include_router(start_router)
    # dp.include_router(free_lesson_form_router)
    dp.include_router(echo_router)

    #обрабатываем все сообщения
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    #запускаем бота
    asyncio.run(main())