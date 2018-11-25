import os
import time
import telebot
from random import randint
from flask import Flask, request
from constants import *

bot = telebot.TeleBot(token)
server = Flask(__name__)
Main_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
Main_mark_up.row('Список задач', 'Поиск')
Main_mark_up.row('Получить задачу по сложности', 'Книги')
Main_mark_up.row('Отправить решение', 'Отправить отзыв')

categories_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
categories_mark_up.row('Легкие', 'Средние', 'Сложные')
categories_mark_up.row('Случайная')
categories_mark_up.row('Отмена')

cancel_mark_up = telebot.types.ReplyKeyboardMarkup(True, False)
cancel_mark_up.row('Отмена')


def get_task_by_number(tasks, number):
    try:
        return next((x for x in tasks if x.number == number), None) 
    except:
        return None


def get_random_task(tasks):
    rand = randint(1, len(tasks))
    if 1 <= rand <= len(tasks):
      return get_task_by_number(tasks, rand)
    else:
      return None


@bot.message_handler(commands=['start'])
def start(message):
    text_of_message = start_command_message
    bot.send_message(message.from_user.id, text_of_message, reply_markup=Main_mark_up)


@bot.message_handler(commands=['help'])
def help(message):
    text_of_message = help_command_message
    bot.send_message(message.from_user.id, text_of_message, reply_markup=Main_mark_up, parse_mode="Markdown")


@bot.message_handler(commands=['about'])
def about(message):
    text_of_message = about_command_message
    bot.send_message(message.from_user.id, text_of_message, reply_markup=Main_mark_up)


@bot.message_handler(regexp='Список задач')
def task_handler(message):
    text_of_message = '*📋 Список задач*\n https://telegra.ph/Unique-Lectures-06-13'
    bot.send_message(message.from_user.id, text_of_message, reply_markup=Main_mark_up, parse_mode="Markdown")


@bot.message_handler(regexp='Получить задачу по сложности')
def get_task(message):
    bot.send_message(message.from_user.id, 'Выберите категорию.', reply_markup=categories_mark_up)
    bot.register_next_step_handler_by_chat_id(message.chat.id, categories)


def categories(message):
    try:
        if 'Случайная' in message.text:
            random_task = get_random_task(task_list)
            text = '*🎲 Задача на удачу:*\n{0}'.format(random_task.announcement_link)
            bot.send_message(message.from_user.id, text, reply_markup=categories_mark_up, parse_mode="Markdown")
            bot.register_next_step_handler_by_chat_id(message.chat.id, categories)
        else:
            text = categories_dict[message.text]
            bot.send_message(message.from_user.id, text, reply_markup=Main_mark_up, parse_mode="Markdown")
    except KeyError:
        text = 'Такой категории нет. Попробуйте еще раз.'
        bot.send_message(message.from_user.id, text, reply_markup=categories_mark_up)
        bot.register_next_step_handler_by_chat_id(message.chat.id, categories)


@bot.message_handler(regexp='Книги')
def books(message):
    bot.send_message(message.from_user.id, books_message, reply_markup=Main_mark_up, parse_mode="Markdown")


@bot.message_handler(regexp='Отправить отзыв')
def review_handler(message):
    bot.send_message(message.from_user.id,
                     'В следующем сообщении введите свой отзыв. Чтобы отменить написание отзыва, введите "Отмена".',
                     reply_markup=cancel_mark_up)
    bot.register_next_step_handler_by_chat_id(message.chat.id, feedback)


def feedback(message):
    if 'Отмена' in message.text:
        bot.send_message(message.from_user.id, 'Вы отменили написание отзыва. Выберите дальнейшее действие.',
                         reply_markup=Main_mark_up)
        return
    time_at_now = time.strftime("%H:%M:%S %Y.%m.%d", time.localtime())
    form = '''Feedback from {0} - @{1} ({2});\nDate: {3};\nText: {4}'''.format(message.from_user.first_name,
                                                                               message.from_user.username,
                                                                               message.from_user.id, 
                                                                               time_at_now,
                                                                               message.text)
    bot.send_message('@unilecs_test', form)
    bot.send_message(message.from_user.id, 'Спасибо за ваш отзыв. Выберите следующее действие.',
                     reply_markup=Main_mark_up)


@bot.message_handler(regexp='Отправить решение')
def answer(message):
    bot.send_message(message.from_user.id,
                     '💡 В следующем сообщении введите свое решение последней опубликованной задачи. Чтобы отменить отправку решения, введите "Отмена".',
                     reply_markup=cancel_mark_up)
    bot.register_next_step_handler_by_chat_id(message.chat.id, solution)


def solution(message):
    if 'Отмена' in message.text:
        bot.send_message(message.from_user.id, 'Вы отменили отправку решения. Выберите дальнейшее действие.',
                         reply_markup=Main_mark_up)
        return
    time_at_now = time.strftime("%H:%M:%S %Y.%m.%d", time.localtime())
    form = '''Feedback from {0} - @{1} ({2});\nDate: {3};\nText: {4}'''.format(message.from_user.first_name,
                                                                               message.from_user.username,
                                                                               message.from_user.id, 
                                                                               time_at_now,
                                                                               message.text)
    bot.send_message('@unilecs_test', form)
    bot.send_message(message.from_user.id, 'Спасибо за ваше решение. Выберите следующее действие.',
                     reply_markup=Main_mark_up)


@bot.message_handler(regexp='Поиск')
def search(message):
    bot.send_message(message.from_user.id, 'Введите название задачи или ее номер.', reply_markup=cancel_mark_up)
    bot.register_next_step_handler_by_chat_id(message.chat.id, search_result)


def search_result(message):
    if 'Отмена' in message.text:
        bot.send_message(message.from_user.id, 'Поиск отменен. Выберите следующее действие.', reply_markup=Main_mark_up)
    elif message.text.isnumeric():
        try:
            task_link = get_task_by_number(task_list, int(message.text)).announcement_link
            text_of_message = '*Task {0}*\n {1}'.format(message.text, task_link)
            bot.send_message(message.from_user.id, text_of_message, reply_markup=Main_mark_up, parse_mode="Markdown")
        except AttributeError:
            bot.send_message(message.from_user.id, 'Задачи с таким номером не найдено. Попробуйте еще раз.',
                             reply_markup=cancel_mark_up)
            bot.register_next_step_handler_by_chat_id(message.chat.id, search_result)
    else:
        text_of_message = ''
        for task in task_list:
            if task.name.lower().find(message.text.lower()) != -1:
                text_of_message += '*Task {0}: {1}*\n{2}\n\n'.format(task.number, task.name, task.announcement_link)
        if text_of_message == '':
            bot.send_message(message.from_user.id, 'Ни одной задачи не найдено. Попробуйте еще раз.',
                             reply_markup=cancel_mark_up)
            bot.register_next_step_handler_by_chat_id(message.chat.id, search_result)
        else:
            try:
                bot.send_message(message.from_user.id, 
                                text_of_message, 
                                reply_markup=Main_mark_up,
                                parse_mode="Markdown")
                bot.send_message(message.from_user.id, 'Выберите следующее действие.', reply_markup=Main_mark_up)
            except Exception:
                bot.send_message(message.from_user.id,
                                 'Найдено слишком много задач. Попробуйте ввести более корректный запрос.',
                                 reply_markup=cancel_mark_up)
                bot.register_next_step_handler_by_chat_id(message.chat.id, search_result)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.send_message(message.from_user.id, 'Простите, я вас не понимаю. Попробуйте еще раз.', reply_markup=Main_mark_up)


@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='YOUR_SERVER' + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
