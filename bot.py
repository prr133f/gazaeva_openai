from telebot.async_telebot import AsyncTeleBot
import dotenv
import os
import asyncio
import api

dotenv.load_dotenv()

bot = AsyncTeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
async def start(msg):
    await bot.send_message(msg.chat.id, "Привет!! Я умею переводить код с одного языка на другой используя GPT модель! Попробуй прислать мне код в формате: \n/translate\nЯзык на котором написан:Язык на который перевести\nКод")


@bot.message_handler(commands=["translate"])
async def translate(msg):
    text = ''.join(msg.text.split('\n')[1:])
    if text == '':
        await bot.send_message(msg.chat.id, "Вы забыли сказать мне что переводить)")
        return
    try:
        lang1, lang2 = text.split(':')[0], text.split(':')[1].split('\n')[0]
        src = ''.join(text.split(':')[1].split('\n')[1:])
    except:
        await bot.send_message(msg.chat.id, "Неверный формат данных. Воспользуйтесь /start")
        return
    
    g = api.GPT(os.getenv('TOKEN'))
    await bot.send_message(msg.chat.id, g.translate(src, lang1, lang2)['choices'][0]['message']['content'])

@bot.message_handler(func=lambda msg: True)
async def random_message(msg):
    await bot.send_message(msg.chat.id, "Пришли мне код в приведенном выше формате. Я могу повторить его по команде /start")
    

asyncio.run(bot.polling())