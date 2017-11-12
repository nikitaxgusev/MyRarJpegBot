import config
import telebot
from PIL import Image
import requests
from io import BytesIO
import urllib
import io
import shutil

bot = telebot.TeleBot(config.token)

START_NOTE='Hello, ! It is a "Hide RAR/ZIP in picture" service.\n' \
           'Please, follow these steps.\n'\
            '1. Upload a .RAR/.ZIP file first\n'\
            '2. Upload any PICTURE.\n'\
            'For Start to use a service,please, use a command "/start" \n'\
            'If you need a help note,please, use a command "/help"\n'\
            'Thank you for attention.Enjoy!'


HELP_NOTE=''
HELP_NOTE1='Something went wrong.\nPLEASE. take a " /help " note, thank you.'

global my_list
my_list=[]

@bot.message_handler(commands=['start'])
def send_welcome_(message):
    chat_id=message.chat.id
    bot.send_message(chat_id,START_NOTE)

@bot.message_handler(commands=['go','help'])
def send_welcome(message):
    chat_id=message.chat.id
    if message.text =='/go':
        mess=bot.send_message(chat_id,"PLEASE. Upload a .rar file.")
    elif message.text=='/help':
        mess = bot.send_message(chat_id, HELP_NOTE)

@bot.message_handler(content_types=['document'])
def handle_upload_any_doc(message):
    try:
            chat_id = message.chat.id
            file_info = bot.get_file(message.document.file_id)
            filePATHinfo = str(file_info.file_path)

            URL = "https://api.telegram.org/file/bot466580545:AAGeWHkinwAd038imVrGvGSg8gf7P2DPVeo/" + file_info.file_path

            with urllib.request.urlopen(URL) as url:
                f = io.BytesIO(url.read())
            my_list.append(f)
            mess=bot.send_message(chat_id,"OK.You have uploaded a rar file. NOW,please, upload any photo.")
           # bot.register_next_step_handler(mess,handle_docs_photo)
    except Exception as exp:
        bot.reply_to(message,HELP_NOTE)

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
 try:
    chat_id = message.chat.id
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    filePATHinfo = str(file_info.file_path)

    URL = "https://api.telegram.org/file/bot466580545:AAGeWHkinwAd038imVrGvGSg8gf7P2DPVeo/" + file_info.file_path

    with urllib.request.urlopen(URL) as url:
        f = io.BytesIO(url.read())

    file = BytesIO()
    image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)

    obj=my_list[0]
    shutil.copyfileobj(f,file)
    shutil.copyfileobj(obj, file)


    file.seek(0)
    bot.send_message(chat_id, "OK.Now get and save a secret photo.")
    bot.send_document(chat_id, file)

 except Exception as exp:
     bot.reply_to(message,HELP_NOTE1)

if __name__ == '__main__':

     bot.polling(none_stop=True)

