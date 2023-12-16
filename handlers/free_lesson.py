# #FSM = Finite state machine - конечный автомат
#
# from aiogram import Router, F, types
# from aiogram.filters import Command
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
#
# free_lesson_form_router = Router()
#
# class Form(StatesGroup):
#     name = State()
#     age = State()
#     course = State()
#     phone = State()
#
# @free_lesson_form_router.message(Command('free lesson'))
# async def start(message: types.Message, state: FSMContext):
#     await state.set_state(Form.name)
#     await message.answer('как вас зовут')
#
# @free_lesson_form_router.message(Form.name)
# async def process_name(message: types.Message, state: FSMContext):
#     if len(message.text) < 3:
#         await message.answer('слишком короткое имя')
#         return
#     else:
#         await state.update_data(name=message.text)
#         await message.answer(f'Спасибо,{message.text}!')
#
#         await state.set_state(Form.age)
#         await message.answer("Сколько вам лет?")
#
#
# @free_lesson_form_router.message(Form.age)
# async def process_age(message: types.Message, state: FSMContext):
#     age = message.text
#     if not age.isdigit():
#         await message.answer('пожалуйста вводите только цифры')
#     elif int(age)<13 or int(age)>80:
#         await message.answer('Пожалуйста вводитье правильный возраст')
#     else:
#         await state.update_data(age)
