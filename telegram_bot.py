import logging 
from aiogram import Bot , Dispatcher , executor , types
from dotenv import load_dotenv
import sys
import os
import openai

class Reference:
    '''
    A class to store previsouly response from the chatGPT API
    '''
    def __init__(self) -> None:
        self.response  = ""

load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")

reference = Reference()

TOKEN = os.getenv("TOKEN")

## Model Name 
MODEL_NAME = "gpt-3.5-turbo"

## Initialize bot and dispacher

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def clear_past():
    '''
    This Function is used to clear the previous context 

    '''
    reference.response = ""

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start`  command
    """
    await message.reply("Hello\n I am Harsh_BOT \n Powered by Harsh Shukla. \n How Can I Assist You ????")
@dp.message_handler(commands=['clear'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/clear`  command
    """
    clear_past()
    await message.reply("I've Cleared the past conversation and context. \n Powered BY HARSH SHUKLA")

@dp.message_handler(commands=['help'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/help`  command
    """
    helper = """
    Hello I am Harsh_bot I can do some of the functionality as follow :
    1. by /start command you can start the conversation \n
    2. by /clear you can clear the past conversation \n
    3. by /help you can take help to read the working of commands \n

    Have a Nice Day .... Powered by Harsh Shukla
"""
    await message.reply(helper)

@dp.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = MODEL_NAME,
        messages = [
            {"role": "assistant", "content": reference.response}, # role assistant
            {"role": "user", "content": message.text} #our query 
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)



if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)

