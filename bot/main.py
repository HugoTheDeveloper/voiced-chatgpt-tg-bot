import telebot

from tools.chat_gpt import chat_with_gpt

from dotenv import load_dotenv
import os


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    bot.reply_to(msg, 'Привет! Я неофициальный представитель ChatGPT в телеграм!'
                      'Если у тебя есть вопросы, можешь задать их мне без лишней мороки.')


@bot.message_handler(func=lambda message: True)
def talk_to_gpt(msg):
    response = chat_with_gpt(msg.text)
    bot.reply_to(msg, response)


if __name__ == '__main__':
    bot.polling(non_stop=True)
