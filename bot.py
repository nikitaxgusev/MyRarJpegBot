import io
import shutil
import urllib
from io import BytesIO
import requests
import telebot
from PIL import Image
import time

#import config

bot = telebot.TeleBot("473012555:AAE2K5S5STVZXYePOTbjG_resbTM6MRYgFY")

START_NOTE='It is a "Hide .RAR in picture" service.\n' \
            'Please, follow these steps:\n'\
            '1. Upload a (.rar, .7z, .zip) FILE.\n'\
            '2. Upload a (.png, .jpg, .jpeg, .bmp) PICTURE.\n'\
            '3. Download a secret file.\n'\
            '4. For getting (.rar, .7z, .zip ) file - change file resolution to "test.(RARFORMAT)"\n'\
            '5. For getting a picture - change file resolution to "rarpic.png"\n\n'\
            'For START to use a service, please, use a command - "/go" \n'\
            'For Help Note, please, use a command  - "/help"\n'\


HELP_NOTE="It is a 'HELP NOTE'. You are here because something went wrong with a bot.\n"\
          "Or you don't know, how to use a bot."\
          'First of all, please, follow steps in the right order. Did you really do it?\n'\
          'Follow:\n'\
            '1. Upload a (.rar, .7z, .zip) FILE.\n'\
            '2. Upload a (.png, .jpg, .jpeg, .bmp) PICTURE.\n'\
            '3. Download a secret file.\n'\
            '4. For getting (.rar, .7z, .zip ) file - change file resolution to "rarpic.(RARFORMAT)"\n'\
            '5. For getting a picture - change file resolution to "test.png"\n\n'\
            'For START using the service - "/go" \n'\
            'For getting WELCOME message - "/welcome" \n'\
            "If the steps didn't help you. Please, help me to find out the problem.\n"\
            "My email: elgolf@mail.ru\n"\
            "Thank you for attention."


global my_list
my_list=[]

@bot.message_handler(commands=['welcome','start'])
def send_welcome_(message):
    chat_id=message.chat.id
    bot.send_message(chat_id,START_NOTE)

@bot.message_handler(commands=['go','help'])
def send_welcome(message):
    chat_id=message.chat.id
    my_list.append(chat_id)
    if message.text =='/go':
        mess=bot.send_message(chat_id,"Upload a RAR file.")
    elif message.text=='/help':
        mess = bot.send_message(chat_id, HELP_NOTE)

@bot.message_handler(content_types=['document'])
def handle_upload_any_doc(message):
    try:
            chat_id = message.chat.id
            file_info = bot.get_file(message.document.file_id)
            filePATHinfo = str(file_info.file_path)
            URL = "https://api.telegram.org/file/bot473012555:AAE2K5S5STVZXYePOTbjG_resbTM6MRYgFY/" + file_info.file_path

            if filePATHinfo.lower().endswith((".rar",".7z",".zip")):
                mess = bot.send_message(chat_id,"Wait...")
                with urllib.request.urlopen(URL) as url:
                    f = io.BytesIO(url.read())
                my_list.append(f)
                bot.send_message(chat_id,"OK.You have uploaded a RAR file.\n NOW,please, upload any photo 'AS A FILE'.")

            if filePATHinfo.lower().endswith((".jpeg",".png",".jpg",".bmp")):
                with urllib.request.urlopen(URL) as url:
                    f = io.BytesIO(url.read())
                time.sleep(4)
                file = BytesIO()
                image = Image.new('RGB', size=(1024, 700), color=(155, 0, 0))
                image.save(file, 'png')
                file.name = 'rarpic.png'
                file.seek(0)

                bot.send_message(chat_id, "Wait...")
                time.sleep(4)
                obj = my_list[0]
                shutil.copyfileobj(f, file)
                time.sleep(4)
                shutil.copyfileobj(obj, file)

                file.seek(0)
                time.sleep(4)
                bot.send_document(chat_id, file, timeout=10000)
                bot.send_message(chat_id, "OK. Now get and save a secret photo.")

    except Exception as exp:
        bot.reply_to(message,HELP_NOTE)
@bot.message_handler(content_types=['photo'])
def handle_pic(message):
            chat_id = message.chat.id
            bot.message(chat_id,'gavno')

if __name__ == '__main__':

     bot.polling(none_stop=True)

