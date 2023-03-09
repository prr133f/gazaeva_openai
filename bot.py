from telebot.async_telebot import AsyncTeleBot
import dotenv
import os
import asyncio
import api

dotenv.load_dotenv()

token = os.getenv('BOT_TOKEN')

bot = AsyncTeleBot(token)

@bot.message_handler(commands=['start'])
async def start(msg):
    await bot.send_message(msg.chat.id, "Привет!! Я умею переводить код с одного языка на другой используя GPT модель! Попробуй прислать мне код в формате: \nЯзык на котором написан:Язык на который перевести\nКод")


@bot.message_handler(func=lambda message: True)
async def translate(msg):
    lang1, lang2 = msg.text.split(':')[0], msg.text.split(':')[1].split('\n')[0]
    src = ''.join(msg.text.split(':')[1].split('\n')[1:])
    g = api.GPT(os.getenv('TOKEN'))

    await bot.send_message(msg.chat.id, g.translate(src, lang1, lang2)['choices'][0]['message']['content'])
    

asyncio.run(bot.polling())