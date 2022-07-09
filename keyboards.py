from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from constants import HELP_BTN, FEEDBACK_BTN

button_help = KeyboardButton(HELP_BTN)
button_feedback = KeyboardButton(FEEDBACK_BTN)
button_taxi = KeyboardButton('Такси')
button_ravkav = KeyboardButton('Автобусы, поезд и пр.')

main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_kb.add(button_help, button_feedback)
