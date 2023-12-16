from aiogram import Router, types
from aiogram.filters import Command
import random
from pathlib import Path


pic_router = Router()

@pic_router.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    ca = []
    p = Path('/Users/bektur/Downloads/cars sample')
    for c in p.iterdir():
        ca.append(c)
    file = types.FSInputFile(random.choice(ca))
    await message.answer_photo(
        photo=file,
    )