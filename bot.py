import io
import shutil
import urllib
from io import BytesIO
import requests
import telebot
from PIL import Image


#import config

bot = telebot.TeleBot("473012555:AAE2K5S5STVZXYePOTbjG_resbTM6MRYgFY")
HELP_NOTE=""


@bot.message_handler(content_types=['document'])
def handler_docs(message):
    try:

       chat_id = message.chat.id
       file_info = bot.get_file(message.document.file_id)
       filePATHinfo = str(file_info.file_path)
       URL = "https://api.telegram.org/file/bot473012555:AAE2K5S5STVZXYePOTbjG_resbTM6MRYgFY/" + file_info.file_path
       with urllib.request.urlopen(URL) as url:
           f = io.BytesIO(url.read())

       bio = BytesIO()
       image=Image.new('RGBA',size=(240,240),color=(255, 80, 80))
       bio.name = 'image.jpeg'
       image.save(bio, 'PNG')

       shutil.copyfileobj(f, bio)

       bio.seek(0)
       bot.send_message(chat_id, "OK.Now get and save a secret photo.")
       bot.send_document(chat_id, bio,timeout=1000)


    except Exception as e:
        bot.reply_to(message, e)

if __name__ == '__main__':

    bot.polling(none_stop=True)