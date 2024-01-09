import logging 
from aiogram import Bot , Dispatcher , executor , types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
# print(API_TOKEN)

## Configure Logging 
logging.basicConfig(level=logging.INFO)

## Initialize bot and dispacher

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start' , 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or `/help` command
    """
    await message.reply("Hello\n I am Harsh_BOT \n Powered by Harsh Shukla")

@dp.message_handler()
async def command_start_handler(message: types.Message):
    """
    This handler answer the echo
    """
    await message.answer(message.text + "\n\n Powered by Harsh Shukla")

if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)
