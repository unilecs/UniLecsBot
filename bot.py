import os
import telebot
from config import *
from data import *
from constants import *
from flask import Flask, request

# bot config
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

data_manager = DataManager()

# Main markup
Main_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
Main_mark_up.row("Задачи", "Головоломки")
Main_mark_up.row("Книги", "Тесты", "События")
Main_mark_up.row("Поиск", "Отправить")

# Send group markup
send_groups_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
send_groups_mark_up.row("Отзыв", "Решение")
send_groups_mark_up.row("Отмена")

# Task group markup
tasks_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
tasks_mark_up.row("Легкие", "Средние", "Сложные")
tasks_mark_up.row("Случайная", "Список задач")
tasks_mark_up.row("Отмена")

# Puzzle group markup
puzzles_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
puzzles_mark_up.row("Случайная")
puzzles_mark_up.row("Отмена")

# Test group markup
tests_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
tests_mark_up.row("C#.Base", "C#.Advanced")
tests_mark_up.row("C#.OOP", "C#.LINQ")
tests_mark_up.row("Отмена")

# Event group markup
events_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
events_mark_up.row("Прошедшие", "Предстоящие")
events_mark_up.row("Отмена")

# Books group markup
books_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
books_mark_up.row("Программирование", "Алгоритмы")
books_mark_up.row("Идеальный программист")
books_mark_up.row("Отмена")

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
@bot.message_handler(commands=["tasks"])
@bot.message_handler(regexp="Задачи")
def get_task(message):
    bot_send_message(message, CHOOSE_CATEGORY, tasks_mark_up, tasks)

@bot.message_handler(commands=["puzzles"])
@bot.message_handler(regexp="Головоломки")
def get_puzzle(message):
    bot_send_message(message, CHOOSE_CATEGORY, puzzles_mark_up, puzzles)

@bot.message_handler(commands=["books"])
@bot.message_handler(regexp="Книги")
def get_books_handler(message):
    bot_send_message(message, CHOOSE_CATEGORY, books_mark_up, books)

@bot.message_handler(commands=["tests"])
@bot.message_handler(regexp="Тесты")
def get_puzzle(message):
    bot_send_message(message, CHOOSE_CATEGORY, tests_mark_up, tests)

@bot.message_handler(commands=["events"])
@bot.message_handler(regexp="События")
def get_event(message):
    bot_send_message(message, CHOOSE_CATEGORY, events_mark_up, events)

@bot.message_handler(commands=["search"])
@bot.message_handler(regexp="Поиск")
def search(message):
    bot_send_message(message, ENTER_TASK_NUMBER, cancel_mark_up, search_result)

@bot.message_handler(commands=["send"])
@bot.message_handler(regexp="Отправить")
def send_handler(message):
    bot_send_message(message, CHOOSE_WHAT_TO_SEND, send_groups_mark_up, send_groups)


# ---------------------------------------
# private functions
# ---------------------------------------
def send_groups(message):
    if "Отзыв" in message.text:
        bot_send_message(message, SEND_FEEDBACK, cancel_mark_up)
        bot.register_next_step_handler_by_chat_id(message.chat.id, send_user_message, SendType.Feedback)            
    elif "Решение" in message.text:
        bot_send_message(message, SEND_SOLUTION, cancel_mark_up)
        bot.register_next_step_handler_by_chat_id(message.chat.id, send_user_message, SendType.Solution)
    elif "Отмена" in message.text:
        bot_send_message(message, CANCEL_SEND_MESSAGE)
    else:
        bot_send_message(message, UNKNOWN_COMMAND_RESPONSE)


def tasks(message):
    try:
        if "Случайная" in message.text:
            text = data_manager.get_random_task()
            bot_send_message(message, text, tasks_mark_up, tasks)
        elif "Отмена" in message.text:
            bot_send_message(message, CANCEL_TASKS)
        else:
            text = data_manager.get_task_list()[message.text]
            bot_send_message(message, text, tasks_mark_up, tasks)
    except KeyError:
        bot_send_message(message, CATEGORY_NOT_FOUND, tasks_mark_up, tasks)


def puzzles(message):
    try:
        if "Случайная" in message.text:
            text = data_manager.get_random_puzzle()
            bot_send_message(message, text, puzzles_mark_up, puzzles)
        elif "Отмена" in message.text:
            bot_send_message(message, CANCEL_PUZZLES)
        else:
            bot_send_message(message, UNKNOWN_COMMAND_RESPONSE)
    except KeyError:
        bot_send_message(message, CATEGORY_NOT_FOUND, puzzles_mark_up, puzzles)


def books(message):
    try:
        if "Отмена" in message.text:
            bot_send_message(message, CANCEL_BOOKS)
        else:
            book_list = data_manager.get_books(message.text)
            bot_send_message(message, book_list, books_mark_up, books)
    except KeyError:
        bot_send_message(message, CATEGORY_NOT_FOUND, books_mark_up, books)


def tests(message):
    try:
        if "Отмена" in message.text:
            bot_send_message(message, CANCEL_TESTS)
        else:
            text = data_manager.get_test(message.text)
            bot_send_message(message, text, tests_mark_up, tests)
    except KeyError:
        bot_send_message(message, CATEGORY_NOT_FOUND, tests_mark_up, tests)


def events(message):
    try:
        if "Прошедшие" in message.text:
            text_result = data_manager.get_past_events()
            bot_send_message(message, text_result, events_mark_up, events)

        elif "Предстоящие" in message.text:
            text_result = data_manager.get_upcoming_events()
            bot_send_message(message, text_result, events_mark_up, events)

        elif "Отмена" in message.text:
            bot_send_message(message, CANCEL_EVENTS)
        else:
            bot_send_message(message, UNKNOWN_COMMAND_RESPONSE)
    except KeyError:
        bot_send_message(message, CATEGORY_NOT_FOUND, events_mark_up, events)


def send_user_message(message, type):
    if "Отмена" in message.text:
        bot_send_message(message, CANCEL_SEND_SOLUTION if type == SendType.Solution else CANCEL_SEND_FEEDBACK)
        return
    bot.send_message(FEEDBACK_CHANNEL_ID, get_feedback_form(message))
    bot_send_message(message, THANKS_FOR_SOLUTION if type == SendType.Solution else THANKS_FOR_FEEDBACK)


def search_result(message):
    if "Отмена" in message.text:
        bot_send_message(message, CANCEL_SEARCH)
    elif message.text.isnumeric():
        try:
            text_of_message = data_manager.get_task_by_number(int(message.text))
            bot_send_message(message, text_of_message)
        except AttributeError:
            bot_send_message(message, TASK_NUMBER_NOT_FOUND, cancel_mark_up, search_result)
    else:
        text_of_message = data_manager.get_tasks_by_search(message.text)
        if text_of_message == "":
            bot_send_message(message, TASK_NOT_FOUND, cancel_mark_up, search_result)
        else:
            try:
                bot_send_message(message, text_of_message)
                bot_send_message(message, CHOOSE_NEXT_ACTION)
            except Exception:
                bot_send_message(message, TOO_MANY_TASKS_FOUND, cancel_mark_up, search_result)


@bot.message_handler(content_types=["text"])
def handle_message(message):
    bot_send_message(message, UNKNOWN_COMMAND_RESPONSE)


def bot_send_message(message, text, reply_markup=Main_mark_up, callback=None):
    bot.send_message(
        message.from_user.id,
        text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    if callback is not None:
        bot.register_next_step_handler_by_chat_id(message.chat.id, callback)

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
