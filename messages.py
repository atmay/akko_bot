from aiogram.utils.markdown import text
from aiogram.utils.emoji import emojize


def get_start_msg():
    msg = emojize("🌿 Шалом!\nДобро пожаловать в Акко \n "
                  "Этот бот поможет получить ответы на частые вопросы о городе \n"
                  "Вот список доступных команд:\n"
                  "\n"
                  "/help - просмотреть список команд\n"
                  "🌿 Легкой абсорбции!")
    return text(msg)


def get_contacts_msg():
    # added HTML markdown because '_' symbol crashes aiogram's text parser
    msg = "<b>Отдел абсорбции при Мэрии:</b>"
    "\n"
    "Часы приема: ВС-ЧТ с 8:30 до 17:00, ПТ и СБ - выходные. \n"
    "Вход с центрального входа в муниципалитет. \n"
    "Адрес: Weizman St 35, Acre https://g.co/kgs/GP8eKn\n"
    "Согласовать посещение можно по предварительному звонку с кураторами: \n"
    "049956237, 049956212, 049956211, 049956240, 049955304\n\n"
    "Большая просьба не звонить кураторам на личные мобильные телефоны после окончания рабочего дня, "
    "если это не жизненно важный вопрос и его решение может подождать до ЗАВТРАШНЕГО ДНЯ.\n\n"
    "<b>Группы и соцсети Акко:</b>"
    "\n"
    "Полезные геоточки по городу: https://www.cityakko.com/ \n"
    "Группа помощи в телеграмме: https://t.me/akko_pomogaem/ \n"
    "Группа Отдела Абсорбции в телеграмме:  https://t.me/acreabsorption/ \n"
    "Барахолка Акко: https://t.me/+klzIweA2zyM1Yjhk\n"
    "Городская группа в фейсбуке: https://www.facebook.com/groups/akkotoday/ \n"
    "Барахолка Акко в фейсбук https://www.facebook.com/groups/2434822740098624/ \n"
    "Вакансии Акко в фейсбук https://www.facebook.com/groups/524957064937240/?ref=share \n"
    return text(msg)


def get_help_msg():
    msg = emojize("🌴 Вот список доступных команд:\n\n"
                  "/contacts - полезные телефоны и адреса\n"
                  "/myvisit - как записаться в МВД через приложение MyVisit (в картинках!)\n"
                  "/transport - такси, РавКав и приложение Moovit\n"
                  "/shops - магазины в Акко и окрестностях\n"
                  "\nНе нашел нужной команды, которую стоит добавить? "
                  "Напиши @atmayatmay об этом - будем улучшать ботика вместе!")
    return text(msg)
