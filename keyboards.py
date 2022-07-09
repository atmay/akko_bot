from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from constants import HELP_BTN, FEEDBACK_BTN, RAVKAV_BTN, TAXI_BTN, TAXI, RAVKAV

# Main keybord
button_help = KeyboardButton(HELP_BTN)
button_feedback = KeyboardButton(FEEDBACK_BTN)

main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_kb.add(button_help, button_feedback)

# Inline keyboards
inline_taxi_btn = InlineKeyboardButton(TAXI_BTN, callback_data=TAXI)
inline_ravkav_btn = InlineKeyboardButton(RAVKAV_BTN, callback_data=RAVKAV)
inline_transport_kb = InlineKeyboardMarkup().add(inline_taxi_btn, inline_ravkav_btn)
