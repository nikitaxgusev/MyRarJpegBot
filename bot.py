import io
import shutil
import urllib
from io import BytesIO
import requests
import telebot
from PIL import Image
<<<<<<< HEAD
=======

>>>>>>> 4db476822b56981be1481e1049d168e81ffc0472


bot = telebot.TeleBot("473012555:AAE2K5S5STVZXYePOTbjG_resbTM6MRYgFY")
HELP_NOTE=""

<<<<<<< HEAD
HELP_NOTE="In order to get a successful result\n" \
          "You should follow the rules:\n"\
          "1. Upload the archive (.rar, .7z, .zip) like a 'Document'\n"\
          "2. Get a result photo\n\n"\
          "IMPORTANT:\n"\
          "If you try to upload a photo, video, voice or audio, you won't get a result photo.\n"\
          "That's why use only 'Document Uploading'"\
          "Your document size shouldn't be bigger than 20 mb\n"\
          "/go - start using"

@bot.message_handler(commands=['help','go','start'])
def send_help(message):
    chat_id=message.chat.id

    if message.text=="/help":
        bot.send_message(chat_id,HELP_NOTE)

    if message.text=="/go":
        bot.send_message(chat_id,"Upload the archive like a 'document'\n")

    if message.text=="/start":
        bot.send_message(chat_id,"Upload the archive like a 'document'\n")


=======
>>>>>>> 4db476822b56981be1481e1049d168e81ffc0472

@bot.message_handler(content_types=['document'])
def handler_docs(message):
    try:
<<<<<<< HEAD

       chat_id = message.chat.id
       file_info = bot.get_file(message.document.file_id)
       filePATHinfo = str(file_info.file_path)
       URL = "https://api.telegram.org/file/bot473012555:AAE2K5S5STVZXYePOTbjG_resbTM6MRYgFY/" + file_info.file_path

       if filePATHinfo.lower().endswith((".rar",".zip",".7z")):
           bot.send_message(chat_id,"Wait... Your archive is uploading.\n")
           with urllib.request.urlopen(URL) as url:
               f = io.BytesIO(url.read())

           bot.send_message(chat_id, "Successful uploading!\n")

           bio = BytesIO()
           image=Image.new('RGBA',size=(1200,800),color=(255, 80, 80))
           bio.name = 'image.png'
           image.save(bio, 'PNG')

           shutil.copyfileobj(f, bio)

           bio.seek(0)
           bot.send_message(chat_id, "Wait a little and get a secret photo.")
           bot.send_document(chat_id, bio,timeout=1000)
       else:
           bot.send_message(chat_id, "Upload a file with format: .rar, .7z, .zip. /help")

    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(content_types=['photo'])
def handler_docs(message):
    chat_id=message.chat.id
    bot.send_message(chat_id, "Please, use document uploading. /help")
=======

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
>>>>>>> 4db476822b56981be1481e1049d168e81ffc0472

@bot.message_handler(content_types=['audio'])
def handler_docs(message):
    chat_id=message.chat.id
    bot.send_message(chat_id, "Please, use document uploading. /help")

@bot.message_handler(content_types=['video'])
def handler_docs(message):
    chat_id=message.chat.id
    bot.send_message(chat_id, "Please, use document uploading. /help")

<<<<<<< HEAD
@bot.message_handler(content_types=['voice'])
def handler_docs(message):
    chat_id=message.chat.id
    bot.send_message(chat_id, "Please, use document uploading. /help")

if __name__ == '__main__':

=======
>>>>>>> 4db476822b56981be1481e1049d168e81ffc0472
    bot.polling(none_stop=True)