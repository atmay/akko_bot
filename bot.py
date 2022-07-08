import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text
from aiogram.utils.emoji import emojize
from aiogram.types import ParseMode

from settings import BOT_TOKEN
from messages import get_contacts_msg, get_help_msg, get_start_msg, get_random_input_msg
from keyboards import greet_kb

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
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=greet_kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = get_help_msg()
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['myvisit'])
async def process_myvisit_command(message: types.Message):
    msg = text(emojize("Выбери, какую запись ты хочешь сделать:\n"
                       ))
    # TODO add buttons for Darkon and Teudat Zeut
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['contacts'])
async def process_contacts_command(message: types.Message):
    msg = get_contacts_msg()
    await message.reply(msg, parse_mode=ParseMode.HTML)


@dp.message_handler(commands=['transport'])
async def process_transport_command(message: types.Message):
    msg = text(emojize("Кучер, запрягай! 🦄\n"
                       "О чем тебе рассказать?\n"
                       ))
    # TODO add buttons for Ravkav, Moovit, taxis
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['shops'])
async def process_shops_command(message: types.Message):
    msg = text(emojize("Что будем покупать?\n"
                       ))
    # TODO add buttons for grocery stores, electronics, home utensils
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler()
async def handle_random_input(message: types.Message):
    """handle any user message"""
    msg = get_random_input_msg()
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
