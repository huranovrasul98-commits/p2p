import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from PIL import Image
import pytesseract

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

def parse_text(text):
    return text  # позже улучшим парсинг

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("P2P бот запущен. Отправь скрин сделки.")

@dp.message_handler(content_types=['photo'])
async def handle_photo(message: Message):
    photo = message.photo[-1]
    file = await bot.download_file_by_id(photo.file_id)

    image = Image.open(file)
    text = pytesseract.image_to_string(image)

    parsed = parse_text(text)

    await message.answer(f"Распознан текст:\n\n{parsed}")

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
