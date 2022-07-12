from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

import constants as cnst

# Main keybord
button_help = KeyboardButton(cnst.HELP_BTN)
button_feedback = KeyboardButton(cnst.FEEDBACK_BTN)

main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_kb.add(button_help, button_feedback)

# Inline keyboards

# transport inline
inline_taxi_btn = InlineKeyboardButton(cnst.TAXI_BTN, callback_data=cnst.TAXI)
inline_ravkav_btn = InlineKeyboardButton(cnst.RAVKAV_BTN, callback_data=cnst.RAVKAV)
inline_transport_kb = InlineKeyboardMarkup(row_width=1).add(inline_taxi_btn, inline_ravkav_btn)

# shops inline
inline_grocery_btn = InlineKeyboardButton(cnst.GROCERY_BTN, callback_data=cnst.GROCERY)
inline_appliances_btn = InlineKeyboardButton(cnst.APPLIANCES_BTN, callback_data=cnst.APPLIANCES)
inline_home_goods_btn = InlineKeyboardButton(cnst.HOME_GOODS_BTN, callback_data=cnst.HOME_GOODS)
inline_office_spls_btn = InlineKeyboardButton(cnst.OFFICE_SUPPLIES_BTN, callback_data=cnst.OFFICE_SUPPLIES)
inline_shops_kb = InlineKeyboardMarkup(row_width=1).add(inline_grocery_btn,
                                                        inline_home_goods_btn,
                                                        inline_appliances_btn,
                                                        inline_office_spls_btn)

# money inline
