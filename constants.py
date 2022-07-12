# commands
TAXI = 'taxi'
RAVKAV = 'ravkav'

FEEDBACK = 'feedback'
HELP = 'help'

GROCERY = 'grocery'
APPLIANCES = 'appliances'
HOME_GOODS = 'homegoods'
OFFICE_SUPPLIES = 'office'

BANK_VISIT = ''
MONEY_EXCHANGE = ''
CORONA_PAY = ''

DARKON = ''
TEUDAT_ZEUT = ''

# buttons
TAXI_BTN = 'Такси'
RAVKAV_BTN = 'Оплата проезда: Равкав'

HELP_BTN = 'Список команд'
FEEDBACK_BTN = 'Обратная связь'

GROCERY_BTN = 'Продукты'
APPLIANCES_BTN = 'Бытовая техника'
HOME_GOODS_BTN = 'Товары для дома'
OFFICE_SUPPLIES_BTN = 'Канцелярия'

BANK_VISIT_BTN = 'Записаться в Дисконт банк'
MONEY_EXCHANGE_BTN = 'Поменять деньги'
CORONA_PAY_BTN = 'Золотая корона: где получить?'

DARKON_BTN = 'Даркон: что это, как оформить'
TEUDAT_ZEUT_BTN = 'Биометрический теудат зеут'

# keybord buttons with related commands
BUTTONS = {
    TAXI_BTN: TAXI,
    RAVKAV_BTN: RAVKAV,
    HELP_BTN: HELP,
    FEEDBACK_BTN: FEEDBACK,
    GROCERY_BTN: GROCERY,
    APPLIANCES_BTN: APPLIANCES,
    HOME_GOODS_BTN: HOME_GOODS,
    OFFICE_SUPPLIES_BTN: OFFICE_SUPPLIES
}

# groups of commands
GROUP_TRANSPORT = [TAXI, RAVKAV]
GROUP_MAIN = [HELP, FEEDBACK]
GROUP_SHOPS = [GROCERY, APPLIANCES, HOME_GOODS, OFFICE_SUPPLIES]
