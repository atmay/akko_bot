import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text
from aiogram.types import ParseMode

import constants as cnst
import messages as m

from settings import BOT_TOKEN
from messages import get_contacts_msg, get_help_msg, get_start_msg, get_random_input_msg, get_taxi_msg, \
    get_feedback_msg, get_transport_msg
from keyboards import main_kb, inline_transport_kb, inline_shops_kb
from constants import BUTTONS, HELP, FEEDBACK

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    msg = get_start_msg()
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=main_kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = get_help_msg()
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['feedback'])
async def process_feedback_command(message: types.Message):
    msg = get_feedback_msg()
    await message.reply(msg, parse_mode=ParseMode.HTML)


@dp.message_handler(commands=['myvisit'])
async def process_myvisit_command(message: types.Message):
    msg = text("Выбери, какую запись ты хочешь сделать:\n"
               )
    # TODO add buttons for Darkon and Teudat Zeut
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['contacts'])
async def process_contacts_command(message: types.Message):
    msg = get_contacts_msg()
    await message.reply(msg, parse_mode=ParseMode.HTML)


@dp.message_handler(commands=['transport'])
async def process_transport_command(message: types.Message):
    if message.text == '/taxi':
        msg = get_taxi_msg()
        await message.reply(msg, parse_mode=ParseMode.MARKDOWN)
    else:
        msg = get_transport_msg()
        await message.reply(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_transport_kb)


@dp.callback_query_handler(lambda c: c.data in cnst.GROUP_TRANSPORT)
async def process_callback_transport(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    command = callback_query.data
    if command == cnst.TAXI:
        msg = m.get_taxi_msg()
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(chat_id=callback_query.from_user.id, text=msg, parse_mode=ParseMode.MARKDOWN)
    elif command == cnst.RAVKAV:
        msg = m.get_ravkav_msg()
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(chat_id=callback_query.from_user.id, text=msg, parse_mode=ParseMode.HTML)
    else:
        await bot.answer_callback_query(callback_query.id)


@dp.message_handler(commands=['shops'])
async def process_shops_command(message: types.Message):
    msg = text("Что будем покупать?\n")
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_shops_kb)


@dp.callback_query_handler(lambda c: c.data in cnst.GROUP_SHOPS)
async def process_callback_shops(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    command = callback_query.data
    if command == cnst.GROCERY:
        msg = m.get_grocery_msg()
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(chat_id=callback_query.from_user.id, text=msg, parse_mode=ParseMode.HTML)
    elif command == cnst.HOME_GOODS:
        msg = m.get_home_goods_msg()
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(chat_id=callback_query.from_user.id, text=msg, parse_mode=ParseMode.HTML)
    elif command == cnst.APPLIANCES:
        msg = m.get_appliances_msg()
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(chat_id=callback_query.from_user.id, text=msg, parse_mode=ParseMode.HTML)
    elif command == cnst.OFFICE_SUPPLIES:
        msg = m.get_office_supplies_msg()
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(chat_id=callback_query.from_user.id, text=msg, parse_mode=ParseMode.HTML)
    else:
        await bot.answer_callback_query(callback_query.id)


@dp.message_handler()
async def handle_random_input(message: types.Message):
    """handle unknown messages and main keyboard"""
    command = BUTTONS.get(message.text)
    if not command:
        msg = get_random_input_msg()
        await message.reply(msg, parse_mode=ParseMode.MARKDOWN)
    else:
        message.text = command
        if command == HELP:
            await process_help_command(message)
        elif command == FEEDBACK:
            await process_feedback_command(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
