import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text, italic, code
from aiogram.utils.emoji import emojize
from aiogram.types import ParseMode

from settings import BOT_TOKEN

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
    msg = text(emojize("🌿 Шалом!\nДобро пожаловать в Акко \n "
                       "Этот бот поможет получить ответы на частые вопросы о городе \n"
                       "Вот список доступных команд:\n"
                       "\n"
                       "/help - просмотреть список команд\n"
                       "🌿 Легкой абсорбции!"))
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(emojize("🌴 Вот список доступных команд:\n\n"
                       "/myvisit - как записаться в МВД через приложение MyVisit (в картинках!)\n"
                       "/transport - такси, РавКав и приложение Moovit\n"
                       "/shops - магазины в Акко и окрестностях\n"
                       "\nНе нашел нужной команды, которую стоит добавить? "
                       "Напиши @atmayatmay об этом - давайте улучшать ботика вместе!"))
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['myvisit'])
async def process_help_command(message: types.Message):
    msg = text(emojize("Выбери, какую запись ты хочешь сделать:\n"
                       ))
    # TODO add buttons for Darkon and Teudat Zeut
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler()
async def echo(message: types.Message):
    """handle any user message"""
    msg = text(emojize('Я не очень умный бот, мне это непонятно 🥺\n'
                       'Жми /help и увидишь список доступных команд \n'))
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
