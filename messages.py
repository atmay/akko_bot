from aiogram.utils.markdown import text, bold
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
    msg = text("<b>Экстренные телефоны</b>\n",
               emojize("⚠️ *4911 - Мокед Ирия Акко\n"
                       "🚓 100 - номер для экстренных вызовов (миштара - полиция)\n"
                       "🚑 101 - скорая помощь (МАДА), но дешевле через больничную кассу\n"
                       "🚒 102 - пожарные и спасатели (кибуй эш)\n"
                       "⚡ 103 - Электрическая Компания (Хеврат Хашмаль)\n"
                       "⚠️ 104 - Служба Тыла (Пикуд ха Ореф)\n"
                       "📳 110 -изр.миштара. информация, выяснения каких-то подробностей и т.д. "
                       "Его придумали, чтобы разгрузить номер 100\n"
                       "🆘 112 - номер, на который можно позвонить с любого мобильного телефона, "
                       "даже если он закрыт на пароль, у него нет симки, он отключен за неуплату и т.д."),
               "\n\n<b>Отдел абсорбции при Мэрии:</b>"
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
               "Вакансии Акко в фейсбук https://www.facebook.com/groups/524957064937240/?ref=share \n")
    return msg


def get_help_msg():
    msg = emojize("🌴 Вот список доступных команд:\n\n"
                  "/contacts - полезные телефоны и адреса\n"
                  "/myvisit - как записаться в МВД через приложение MyVisit (в картинках!)\n"
                  "/transport - такси, РавКав и приложение Moovit\n"
                  "/shops - магазины в Акко и окрестностях\n"
                  "/feedback - обратная связь, предложения по развитию ботика\n"
                  "\n"
                  "А еще! В правом нижнем углу под кнопкой в виде квадрата с кнопками внутри - клавиатура с базовыми командами.\n")
    return text(msg)


def get_feedback_msg():
    msg = "🐸 Не нашел нужной команды, которую стоит добавить?\n" \
          "Хочешь добавить полезную информацию?\n\n" \
          "👇\n" \
          "<b>Напиши @atmayatmay об этом - будем улучшать ботика вместе!</b>"
    return text(msg)


def get_random_input_msg():
    msg = emojize('Я пока еще не очень умный бот, мне это непонятно 🥺\n\n'
                  'Посмотреть, что я умею ➡ /help \n'
                  'Оставить обратную связь ➡ /feedback ')
    return text(msg)


def get_transport_msg():
    msg = text(emojize("Кучер, запрягай! 🦄\n"
                       "О чем тебе рассказать?\n"
                       ))
    return msg


def get_taxi_msg():
    msg = text(bold("Такси на русском:\n"),
               "0545973414 Илья\n"
               "0526040920 Сергей\n"
               "0522693789 Герман\n"
               "0507179379 Виктор\n"
               "0542108723 Свильям\n"
               "0504062620 Виталий\n"
               "0505921939 Алекс\n\n",
               bold("Такси на иврите:\n"),
               "049816666\n"
               "049910111")
    return msg
