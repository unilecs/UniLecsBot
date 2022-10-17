import os
import telebot
from data import *
from utils import *
from constants import *
from flask import Flask, request

# ENV variables
FEEDBACK_CHANNEL_ID = os.environ["FEEDBACK_CHANNEL_ID"]
TOKEN = os.environ["BOT_TOKEN"]
BASE_URL = os.environ["BASE_URL"]
SERVER_URL = BASE_URL + TOKEN

# bot config
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
data_service = DataService()

# Main markup
Main_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
Main_mark_up.row("Список задач", "Поиск")
Main_mark_up.row("Получить задачу по сложности", "Книги")
Main_mark_up.row("Отправить")

# Send group markup
send_groups_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
send_groups_mark_up.row("Отзыв", "Решение")
send_groups_mark_up.row("Отмена")

# Task group markup
categories_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
categories_mark_up.row("Легкие", "Средние", "Сложные")
categories_mark_up.row("Случайная")
categories_mark_up.row("Отмена")

# Cancel markup
cancel_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
cancel_mark_up.row("Отмена")

# ---------------------------------------
# bot commands
# ---------------------------------------
@bot.message_handler(commands=["start"])
def start(message):
    bot_send_message(message, WELCOME)


@bot.message_handler(commands=["help"])
def help(message):
    bot_send_message(message, HELP)


@bot.message_handler(commands=["about"])
def about(message):
    bot_send_message(message, ABOUT)


# ---------------------------------------
# Main markup
# ---------------------------------------
@bot.message_handler(regexp="Список задач")
def task_handler(message):
    bot_send_message(message, data_service.get_all_tasks_link())


@bot.message_handler(regexp="Поиск")
def search(message):
    bot_send_message(message, ENTER_TASK_NUMBER, cancel_mark_up)
    bot.register_next_step_handler_by_chat_id(message.chat.id, search_result)


@bot.message_handler(regexp="Получить задачу по сложности")
def get_task(message):
    bot_send_message(message, CHOOSE_CATEGORY, categories_mark_up)
    bot.register_next_step_handler_by_chat_id(message.chat.id, categories)


@bot.message_handler(regexp="Книги")
def books(message):
    bot_send_message(message, data_service.get_books_message())


@bot.message_handler(regexp="Отправить")
def send_handler(message):
    bot_send_message(message, CHOOSE_WHAT_TO_SEND, send_groups_mark_up)
    bot.register_next_step_handler_by_chat_id(message.chat.id, send_groups)


# ---------------------------------------
# private functions
# ---------------------------------------
def send_groups(message):
    if "Отзыв" in message.text:
        bot_send_message(message, SEND_FEEDBACK, cancel_mark_up)
        bot.register_next_step_handler_by_chat_id(message.chat.id, feedback)            
    elif "Решение" in message.text:
        bot_send_message(message, SEND_SOLUTION, cancel_mark_up)
        bot.register_next_step_handler_by_chat_id(message.chat.id, solution)
    elif "Отмена" in message.text:
        bot_send_message(message, CANCEL_SEND_MESSAGE)
    else:
        bot_send_message(message, UNKNOWN_COMMAND_RESPONSE)


def categories(message):
    try:
        if "Случайная" in message.text:
            random_task = get_random_task(data_service.get_tasks())
            text = "*🎲 Задача на удачу:*\n{0}".format(random_task.announcement_link)
            bot_send_message(message, text, categories_mark_up)
            bot.register_next_step_handler_by_chat_id(message.chat.id, categories)
        else:
            text = data_service.get_categories_dict()[message.text]
            bot_send_message(message, text)
    except KeyError:
        bot_send_message(message, CATEGORY_NOT_FOUND, categories_mark_up)
        bot.register_next_step_handler_by_chat_id(message.chat.id, categories)


def feedback(message):
    if "Отмена" in message.text:
        bot_send_message(message, CANCEL_SEND_FEEDBACK)
        return
    bot.send_message(FEEDBACK_CHANNEL_ID, get_feedback_form(message))
    bot_send_message(message, THANKS_FOR_FEEDBACK)


def solution(message):
    if "Отмена" in message.text:
        bot_send_message(message, CANCEL_SEND_SOLUTION)
        return
    bot.send_message(FEEDBACK_CHANNEL_ID, get_feedback_form(message))
    bot_send_message(message, THANKS_FOR_SOLUTION)


def search_result(message):
    if "Отмена" in message.text:
        bot_send_message(message, CANCEL_SEARCH)
    elif message.text.isnumeric():
        try:
            task_link = get_task_by_number(
                data_service.get_tasks(), int(message.text)
            ).announcement_link
            text_of_message = "*Task {0}*\n {1}".format(message.text, task_link)
            bot_send_message(message, text_of_message)
        except AttributeError:
            bot_send_message(message, TASK_NUMBER_NOT_FOUND, cancel_mark_up)
            bot.register_next_step_handler_by_chat_id(message.chat.id, search_result)
    else:
        text_of_message = ""
        for _task in data_service.get_tasks():
            if _task.name.lower().find(message.text.lower()) != -1:
                text_of_message += "*Task {0}: {1}*\n{2}\n\n".format(
                    _task.number, _task.name, _task.announcement_link
                )
        if text_of_message == "":
            bot_send_message(message, TASK_NOT_FOUND, cancel_mark_up)
            bot.register_next_step_handler_by_chat_id(message.chat.id, search_result)
        else:
            try:
                bot_send_message(message, text_of_message)
                bot_send_message(message, CHOOSE_NEXT_ACTION)
            except Exception:
                bot_send_message(message, TOO_MANY_TASKS_FOUND, cancel_mark_up)
                bot.register_next_step_handler_by_chat_id(
                    message.chat.id, search_result
                )


@bot.message_handler(content_types=["text"])
def handle_message(message):
    bot_send_message(message, UNKNOWN_COMMAND_RESPONSE)

def bot_send_message(message, text, reply_markup=Main_mark_up, parse_mode="Markdown"):
    bot.send_message(
        message.from_user.id,
        text,
        reply_markup=reply_markup,
        parse_mode=parse_mode
    )

# ---------------------------------------
# bot webhook
# ---------------------------------------

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=SERVER_URL)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

'''
# test locally with infinity pooling
if __name__ == "__main__":
    bot.polling(none_stop=True)
'''
