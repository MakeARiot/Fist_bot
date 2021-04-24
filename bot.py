import telebot
from telebot import types
import config
import infa
from operator import itemgetter
import time
from collections import defaultdict

bot = telebot.TeleBot(config.BOT_TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Главное меню бота\U0001F916')

ist = 0
moiais = 0
ivt = 0
ping = 0
uvts = 0
pinf = 0
i = 0
bi = 0
rso = 0

user_id = defaultdict(lambda: { 'ist': 0, 'moiais': 0, 'ivt': 0, 'ping': 0, 'uvts': 0, 'pinf': 0, 'i': 0, 'bi': 0, 'rso': 0})

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="О ФИСТ", callback_data="o_fist")
    btn2 = types.InlineKeyboardButton(text="Кафедры", callback_data="deportment")
    btn3 = types.InlineKeyboardButton(text="Пройти опрос", callback_data="survey_ekz")
    btn4 = types.InlineKeyboardButton(text="Показать на карте", callback_data="location")
    btn5 = types.InlineKeyboardButton(text="Контакты", callback_data="contacts")
    btn6 = types.InlineKeyboardButton(text="Полезные ссылки", callback_data="links")
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANzX8qB2yAi_MNdJ-DPXO_nVk23iC8AAm8AA9vbfgABmVtQqHuTgHQeBA')
    bot.send_message(message.chat.id, "Привет, "+ str(message.from_user.first_name)+"!", reply_markup=keyboard1)
    
    bot.send_message(message.chat.id, "Я бот, который поможет тебе узнать о факультете ИСТ, кафедрах этого факультета, а также поможет определиться с выбором направления подготовки.\n\nДля начала нажми кнопку ниже\U0001F447", reply_markup=keyboard)
   

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global ist 
    global moiais 
    global ivt 
    global ping 
    global uvts 
    global pinf 
    global i 
    global bi 
    global rso 
    
    global user_id

    user_id_key = call.message.chat.id

    if call.data == "o_fist":
        keyboard = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton('Назад', callback_data='back')
        btn1 = types.InlineKeyboardButton('Научные направления', callback_data='activities')
        btn2 = types.InlineKeyboardButton('Направления подготовки', callback_data='training')
        keyboard.add(btn0)
        keyboard.add(btn1, btn2)
        bot.send_message(call.message.chat.id, infa.o_fist, reply_markup=keyboard, parse_mode='Markdown')

    if call.data == "back":
       
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    

    if call.data == "activities":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        btn2 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
        
        keyboard.add(btn1)
        keyboard.add(btn2)
        bot.send_message(call.message.chat.id, infa.activities, reply_markup=keyboard, parse_mode='Markdown')

    if call.data == "training":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        btn2 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
        # btn2 = types.InlineKeyboardButton('Направления подготовки', callback_data='training')

        keyboard.add(btn1)
        keyboard.add(btn2)
        bot.send_message(call.message.chat.id, infa.training, reply_markup=keyboard, parse_mode='Markdown')    

    if call.data == "main_menu":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="О ФИСТ", callback_data="o_fist")
        btn2 = types.InlineKeyboardButton(text="Кафедры", callback_data="deportment")
        btn3 = types.InlineKeyboardButton(text="Пройти опрос", callback_data="survey_ekz")
        btn4 = types.InlineKeyboardButton(text="Показать на карте", callback_data="location")
        btn5 = types.InlineKeyboardButton(text="Контакты", callback_data="contacts")
        btn6 = types.InlineKeyboardButton(text="Полезные ссылки", callback_data="links")
        btn0 = types.InlineKeyboardButton('Назад', callback_data='back')
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        keyboard.add(btn5)
        keyboard.add(btn6)	
        keyboard.add(btn0)
        bot.send_message(call.message.chat.id, '*Главное меню:*', reply_markup=keyboard, parse_mode='Markdown')       

    if call.data == "deportment":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(infa.deportment[3], callback_data='deportment0')
        btn2 = types.InlineKeyboardButton(infa.deportment[1], callback_data='deportment1')
        btn3 = types.InlineKeyboardButton(infa.deportment[2], callback_data='deportment2')
        btn4 = types.InlineKeyboardButton(infa.deportment[0], callback_data='deportment3')
        btn5 = types.InlineKeyboardButton(infa.deportment[4], callback_data='deportment4')
        btn6 = types.InlineKeyboardButton(infa.deportment[5], callback_data='deportment5')
        btn7 = types.InlineKeyboardButton(infa.deportment[6], callback_data='deportment6')
        btn0 = types.InlineKeyboardButton('Назад', callback_data='back')       
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        keyboard.add(btn5)
        keyboard.add(btn6)
        keyboard.add(btn7)
        keyboard.add(btn0)
        
        bot.send_message(call.message.chat.id, '*Для просмотра подробной информации о кафедре, \nнажмите ниже*\U0001F447', reply_markup=keyboard, parse_mode='Markdown') 


    if call.data == "deportment3":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        # btn2 = types.InlineKeyboardButton('<', callback_data='kaf6')
        btn3 = types.InlineKeyboardButton('Контакты', callback_data='deportment_contacts3')
        keyboard.add(btn1)
        keyboard.add(btn3)
        
        bot.send_message(call.message.chat.id, infa.deportment0, reply_markup=keyboard, parse_mode='Markdown')  

    if call.data == "deportment_contacts3":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')

        keyboard.add(btn1)

        # bot.send_message(call.message.chat.id, infa.deportment_contacts0, reply_markup=keyboard, parse_mode='Markdown')   
        bot.send_photo(call.message.chat.id, 'http://fist.psuti.ru/employees/picture/93', caption=infa.deportment_contacts0, reply_markup=keyboard, parse_mode='Markdown')
        # bot.send_message(call.message.chat.id, infa.deportment_contacts0, )    


    if call.data == "deportment1":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        
        btn3 = types.InlineKeyboardButton('Контакты', callback_data='deportment_contacts1')
        keyboard.add(btn1)
        keyboard.add(btn3)
        
        bot.send_message(call.message.chat.id, infa.deportment1, reply_markup=keyboard, parse_mode='Markdown')  

    if call.data == "deportment_contacts1":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')

        keyboard.add(btn1)
   
        bot.send_photo(call.message.chat.id, 'http://fist.psuti.ru/employees/picture/94', caption=infa.deportment_contacts1, reply_markup=keyboard, parse_mode='html')
  
    

    if call.data == "deportment2":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        # btn2 = types.InlineKeyboardButton('<', callback_data='kaf6')
        btn3 = types.InlineKeyboardButton('Контакты', callback_data='deportment_contacts2')
        keyboard.add(btn1)
        keyboard.add(btn3)
        
        bot.send_message(call.message.chat.id, infa.deportment2, reply_markup=keyboard, parse_mode='Markdown')  

    if call.data == "deportment_contacts2":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')

        keyboard.add(btn1)

        # bot.send_message(call.message.chat.id, infa.deportment_contacts0, reply_markup=keyboard, parse_mode='Markdown')   
        bot.send_photo(call.message.chat.id, 'http://fist.psuti.ru/employees/picture/95', caption=infa.deportment_contacts2, reply_markup=keyboard, parse_mode='Markdown')
        # bot.send_message(call.message.chat.id, infa.deportment_contacts0, )              
    
    if call.data == "deportment0":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        # btn2 = types.InlineKeyboardButton('<', callback_data='kaf6')
        btn3 = types.InlineKeyboardButton('Контакты', callback_data='deportment_contacts0')
        keyboard.add(btn1)
        keyboard.add(btn3)
        
        bot.send_message(call.message.chat.id, infa.deportment3, reply_markup=keyboard, parse_mode='Markdown')  

    if call.data == "deportment_contacts0":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')

        keyboard.add(btn1)

        # bot.send_message(call.message.chat.id, infa.deportment_contacts0, reply_markup=keyboard, parse_mode='Markdown')   
        bot.send_photo(call.message.chat.id, 'http://fist.psuti.ru/employees/picture/96', caption=infa.deportment_contacts3, reply_markup=keyboard, parse_mode='Markdown')
        # bot.send_message(call.message.chat.id, infa.deportment_contacts0, )              

    if call.data == "deportment4":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        # btn2 = types.InlineKeyboardButton('<', callback_data='kaf6')
        btn3 = types.InlineKeyboardButton('Контакты', callback_data='deportment_contacts4')
        keyboard.add(btn1)
        keyboard.add(btn3)
        
        bot.send_message(call.message.chat.id, infa.deportment4, reply_markup=keyboard, parse_mode='Markdown')  

    if call.data == "deportment_contacts4":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')

        keyboard.add(btn1)

        # bot.send_message(call.message.chat.id, infa.deportment_contacts0, reply_markup=keyboard, parse_mode='Markdown')   
        bot.send_photo(call.message.chat.id, 'http://fist.psuti.ru/employees/picture/97', caption=infa.deportment_contacts4, reply_markup=keyboard, parse_mode='Markdown')
        # bot.send_message(call.message.chat.id, infa.deportment_contacts0, )              
        
    if call.data == "deportment5":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        # btn2 = types.InlineKeyboardButton('<', callback_data='kaf6')
        btn3 = types.InlineKeyboardButton('Контакты', callback_data='deportment_contacts5')
        keyboard.add(btn1)
        keyboard.add(btn3)
        
        bot.send_message(call.message.chat.id, infa.deportment5, reply_markup=keyboard, parse_mode='Markdown')  

    if call.data == "deportment_contacts5":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')

        keyboard.add(btn1)
        bot.send_photo(call.message.chat.id, 'http://fist.psuti.ru/employees/picture/383', caption=infa.deportment_contacts5, reply_markup=keyboard, parse_mode='Markdown')

    if call.data == "deportment6":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        # btn2 = types.InlineKeyboardButton('<', callback_data='kaf6')
        btn3 = types.InlineKeyboardButton('Контакты', callback_data='deportment_contacts6')
        keyboard.add(btn1)
        keyboard.add(btn3)
        
        bot.send_message(call.message.chat.id, infa.deportment6, reply_markup=keyboard, parse_mode='Markdown')  

    if call.data == "deportment_contacts6":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')

        keyboard.add(btn1)    

        bot.send_photo(call.message.chat.id, 'http://fist.psuti.ru/employees/picture/381', caption=infa.deportment_contacts6, reply_markup=keyboard, parse_mode='html')


    if call.data == "location":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        btn2 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
       
        keyboard.add(btn1)
        keyboard.add(btn2)
        
        bot.send_venue(call.message.chat.id,  latitude=53.2255639, longitude=50.194217714796, title='Поволжский государственный университет телекоммуникаций и информатики\n', address='Московское ш., д. 77, комн. 201, Самара, Самарская обл., 443090', reply_markup=keyboard)     
    

    if call.data == "contacts":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Назад', callback_data='back')
        btn2 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
        keyboard.add(btn1)
        keyboard.add(btn2)
        
        bot.send_message(call.message.chat.id, infa.inline_contacts, reply_markup=keyboard, parse_mode='Markdown')   

    if call.data == "links":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Официальный сайт приемной комиссии', url='https://abitur.psuti.ru/')
        btn2 = types.InlineKeyboardButton(text='Приемная комиссия в Instagram', url='https://www.instagram.com/psuti_abitur/')
        btn3 = types.InlineKeyboardButton(text='Официальный сайт ПГУТИ', url='https://www.psuti.ru/')
        btn4 = types.InlineKeyboardButton(text='Официальный сайт ФИСТ', url='https://www.psuti.ru/ru/faculty/fist')
        btn5 = types.InlineKeyboardButton(text='ФИСТ в VK', url='https://vk.com/fist_psuti')
        btn6 = types.InlineKeyboardButton(text='ФИСТ в Instagram', url='https://www.instagram.com/fist.psuti/')
        btn7 = types.InlineKeyboardButton('Назад', callback_data='back')
        btn8 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')

        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        keyboard.add(btn5)
        keyboard.add(btn6)
        keyboard.add(btn7)
        keyboard.add(btn8)

        bot.send_message(call.message.chat.id, "*Полезные ссылки*\n\nЧтобы перейти на сайт, нажмите кнопку ниже\U0001F447", reply_markup = keyboard, parse_mode='Markdown')


                         
    # if call.data == "kaf2":
    #     keyboard = types.InlineKeyboardMarkup()
    #     btn1 = types.InlineKeyboardButton('ivt', callback_data='pwd1')
    #     btn2 = types.InlineKeyboardButton('<', callback_data='kaf6')
    #     btn3 = types.InlineKeyboardButton('>', callback_data='kaf2')
    #     keyboard.add(btn1)
    #     keyboard.add(btn2, btn3)
        
    #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='infa.deportment2', reply_markup=keyboard, parse_mode='Markdown')  
 # question 1 =============================================================================================================================================================================== 
    
    if call.data == "survey_ekz":
        
        user_id[user_id_key]['ist'] = 0
        user_id[user_id_key]['moiais'] = 0
        user_id[user_id_key]['ivt'] = 0
        user_id[user_id_key]['ping'] = 0
        user_id[user_id_key]['uvts'] = 0
        user_id[user_id_key]['pinf'] = 0
        user_id[user_id_key]['i'] = 0
        user_id[user_id_key]['bi'] = 0
        user_id[user_id_key]['rso'] = 0
        
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer1_question2_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer1_question2_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer1_question2_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer1_question2_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer1_question2_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer1_question2_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer1_question2_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer1_question2_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer1_question2_btn9')
        btn10 = types.InlineKeyboardButton('10', callback_data='answer1_question2_btn10')
        btn11 = types.InlineKeyboardButton('11', callback_data='answer1_question2_btn11')
        btn12 = types.InlineKeyboardButton('12', callback_data='answer1_question2_btn12')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
       
        bot.send_message(call.message.chat.id, infa.question[1], reply_markup=keyboard, parse_mode='Markdown')        

# question 2
    if call.data == "answer1_question2_btn1":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['pinf'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1] + 'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
    
    if call.data == "answer1_question2_btn2":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['pinf'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
    
    if call.data == "answer1_question2_btn3":

        user_id[user_id_key]['ist'] += 1
   

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   

    if call.data == "answer1_question2_btn4":

        user_id[user_id_key]['moiais'] += 1
        user_id[user_id_key]['ivt'] += 1
        user_id[user_id_key]['ping'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
 
    if call.data == "answer1_question2_btn5":

        user_id[user_id_key]['moiais'] += 1
        user_id[user_id_key]['ivt'] += 1
        user_id[user_id_key]['ping'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
    
    if call.data == "answer1_question2_btn6":

        user_id[user_id_key]['ivt'] += 1
      

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 6*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
    
    if call.data == "answer1_question2_btn7":

        user_id[user_id_key]['uvts'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 7*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   

    if call.data == "answer1_question2_btn8":

        
        user_id[user_id_key]['pinf'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 8*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso 

    if call.data == "answer1_question2_btn9":

        user_id[user_id_key]['i'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 9*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
    
    if call.data == "answer1_question2_btn10":

        user_id[user_id_key]['bi'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 10*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
    
    if call.data == "answer1_question2_btn11":

        user_id[user_id_key]['bi'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 11*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   

    if call.data == "answer1_question2_btn12":
    
        user_id[user_id_key]['rso'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer2_question3_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1]+'Вы выбрали *вариант 12*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[2], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso    
         
# question 3    
    if call.data == "answer2_question3_btn1":

        user_id[user_id_key]['ist'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer3_question4_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer3_question4_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer3_question4_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer3_question4_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer3_question4_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer3_question4_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer3_question4_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer3_question4_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer3_question4_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[2]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[3], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
    
    if call.data == "answer2_question3_btn2":

        user_id[user_id_key]['moiais'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer3_question4_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer3_question4_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer3_question4_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer3_question4_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer3_question4_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer3_question4_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer3_question4_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer3_question4_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer3_question4_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[2]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[3], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   

    if call.data == "answer2_question3_btn3":

        user_id[user_id_key]['ivt'] += 1
        user_id[user_id_key]['ping'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer3_question4_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer3_question4_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer3_question4_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer3_question4_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer3_question4_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer3_question4_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer3_question4_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer3_question4_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer3_question4_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[2]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[3], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
        
    if call.data == "answer2_question3_btn4":

        user_id[user_id_key]['uvts'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer3_question4_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer3_question4_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer3_question4_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer3_question4_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer3_question4_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer3_question4_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer3_question4_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer3_question4_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer3_question4_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[2]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[3], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
        
    if call.data == "answer2_question3_btn5":

        user_id[user_id_key]['pinf'] += 1
       
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer3_question4_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer3_question4_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer3_question4_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer3_question4_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer3_question4_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer3_question4_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer3_question4_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer3_question4_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer3_question4_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[2]+'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[3], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
        
    if call.data == "answer2_question3_btn6":

        user_id[user_id_key]['i'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer3_question4_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer3_question4_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer3_question4_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer3_question4_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer3_question4_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer3_question4_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer3_question4_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer3_question4_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer3_question4_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[2]+'Вы выбрали *вариант 6*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[3], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
        
    if call.data == "answer2_question3_btn7":

        user_id[user_id_key]['bi'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer3_question4_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer3_question4_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer3_question4_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer3_question4_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer3_question4_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer3_question4_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer3_question4_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer3_question4_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer3_question4_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[2]+'Вы выбрали *вариант 7*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[3], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   
        
    if call.data == "answer2_question3_btn8":

        user_id[user_id_key]['rso'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer3_question4_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer3_question4_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer3_question4_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer3_question4_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer3_question4_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer3_question4_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer3_question4_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer3_question4_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer3_question4_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[2]+'Вы выбрали *вариант 8*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[3], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso                           

# question 4
    if call.data == "answer3_question4_btn1":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['uvts'] += 1
        user_id[user_id_key]['i'] += 1


        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer4_question5_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer4_question5_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer4_question5_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer4_question5_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer4_question5_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer4_question5_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer4_question5_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer4_question5_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer4_question5_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[3]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[4], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer3_question4_btn2":

        user_id[user_id_key]['moiais'] += 1
        user_id[user_id_key]['ping'] += 1
        user_id[user_id_key]['ivt'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer4_question5_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer4_question5_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer4_question5_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer4_question5_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer4_question5_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer4_question5_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer4_question5_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer4_question5_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer4_question5_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[3]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[4], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso     

    if call.data == "answer3_question4_btn3":

        user_id[user_id_key]['pinf'] += 1
        
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer4_question5_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer4_question5_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer4_question5_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer4_question5_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer4_question5_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer4_question5_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer4_question5_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer4_question5_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer4_question5_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[3]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[4], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso 

    if call.data == "answer3_question4_btn4":

     
        user_id[user_id_key]['bi'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer4_question5_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer4_question5_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer4_question5_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer4_question5_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer4_question5_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer4_question5_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer4_question5_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer4_question5_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer4_question5_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[3]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[4], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso

    if call.data == "answer3_question4_btn5":

        user_id[user_id_key]['rso'] += 1
       
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer4_question5_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer4_question5_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer4_question5_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer4_question5_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer4_question5_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer4_question5_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer4_question5_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer4_question5_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer4_question5_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[3]+'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[4], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso          

# question 5
    if call.data == "answer4_question5_btn1":

        user_id[user_id_key]['i'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer5_question6_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer5_question6_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer5_question6_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer5_question6_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer5_question6_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer5_question6_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer5_question6_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer5_question6_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer5_question6_btn9')
        keyboard.add(btn1, btn2, btn3)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[4]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[5], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso

    if call.data == "answer4_question5_btn2":

        user_id[user_id_key]['ist'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer5_question6_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer5_question6_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer5_question6_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer5_question6_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer5_question6_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer5_question6_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer5_question6_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer5_question6_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer5_question6_btn9')
        keyboard.add(btn1, btn2, btn3)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[4]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[5], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer4_question5_btn3":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['ivt'] += 1
        user_id[user_id_key]['moiais'] += 1
        user_id[user_id_key]['ping'] += 1
        user_id[user_id_key]['pinf'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer5_question6_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer5_question6_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer5_question6_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer5_question6_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer5_question6_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer5_question6_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer5_question6_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer5_question6_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer5_question6_btn9')
        keyboard.add(btn1, btn2, btn3)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[4]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[5], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso    

    if call.data == "answer4_question5_btn4":

        user_id[user_id_key]['bi'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer5_question6_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer5_question6_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer5_question6_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer5_question6_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer5_question6_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer5_question6_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer5_question6_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer5_question6_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer5_question6_btn9')
        keyboard.add(btn1, btn2, btn3)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[4]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[5], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso        

    if call.data == "answer4_question5_btn5":

        user_id[user_id_key]['rso'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer5_question6_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer5_question6_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer5_question6_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer5_question6_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer5_question6_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer5_question6_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer5_question6_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer5_question6_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer5_question6_btn9')
        keyboard.add(btn1, btn2, btn3)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[4]+'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[5], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso 

    if call.data == "answer4_question5_btn6":

        user_id[user_id_key]['uvts'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer5_question6_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer5_question6_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer5_question6_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer5_question6_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer5_question6_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer5_question6_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer5_question6_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer5_question6_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer5_question6_btn9')
        keyboard.add(btn1, btn2, btn3)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[4]+'Вы выбрали *вариант 6*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[5], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso 

# question 6
    if call.data == "answer5_question6_btn1":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['moiais'] += 1 
        user_id[user_id_key]['ivt'] += 1 
        user_id[user_id_key]['ping'] += 1
        user_id[user_id_key]['uvts'] += 1 
        user_id[user_id_key]['pinf'] += 1 
        user_id[user_id_key]['i'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer6_question7_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer6_question7_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer6_question7_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer6_question7_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer6_question7_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer6_question7_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer6_question7_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer6_question7_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer6_question7_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[5]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[6], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso                      

    if call.data == "answer5_question6_btn2":

        user_id[user_id_key]['rso'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer6_question7_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer6_question7_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer6_question7_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer6_question7_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer6_question7_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer6_question7_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer6_question7_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer6_question7_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer6_question7_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[5]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[6], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso    

    if call.data == "answer5_question6_btn3":

        user_id[user_id_key]['bi'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer6_question7_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer6_question7_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer6_question7_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer6_question7_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer6_question7_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer6_question7_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer6_question7_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer6_question7_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer6_question7_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[5]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[6], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso    

# question 7
    if call.data == "answer6_question7_btn1":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['pinf'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer7_question8_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer7_question8_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer7_question8_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer7_question8_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer7_question8_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer7_question8_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer7_question8_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer7_question8_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer7_question8_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[6]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[7], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer6_question7_btn2":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['moiais'] += 1 
        user_id[user_id_key]['ivt'] += 1 
        user_id[user_id_key]['ping'] += 1
        user_id[user_id_key]['pinf'] += 1 
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer7_question8_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer7_question8_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer7_question8_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer7_question8_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer7_question8_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer7_question8_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer7_question8_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer7_question8_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer7_question8_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[6]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[7], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer6_question7_btn3":

        user_id[user_id_key]['ist'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer7_question8_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer7_question8_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer7_question8_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer7_question8_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer7_question8_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer7_question8_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer7_question8_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer7_question8_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer7_question8_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[6]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[7], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer6_question7_btn4":

        user_id[user_id_key]['rso'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer7_question8_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer7_question8_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer7_question8_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer7_question8_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer7_question8_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer7_question8_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer7_question8_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer7_question8_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer7_question8_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[6]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[7], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  
        
    if call.data == "answer6_question7_btn5":

        user_id[user_id_key]['i'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer7_question8_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer7_question8_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer7_question8_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer7_question8_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer7_question8_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer7_question8_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer7_question8_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer7_question8_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer7_question8_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[6]+'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[7], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  
        
    if call.data == "answer6_question7_btn6":

        user_id[user_id_key]['bi'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer7_question8_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer7_question8_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer7_question8_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer7_question8_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer7_question8_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer7_question8_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer7_question8_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer7_question8_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer7_question8_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[6]+'Вы выбрали *вариант 6*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[7], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso              



# question 8
    if call.data == "answer7_question8_btn1":

        user_id[user_id_key]['rso'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer8_question9_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer8_question9_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer8_question9_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer8_question9_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer8_question9_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer8_question9_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer8_question9_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer8_question9_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer8_question9_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[7]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[8], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  
    
    if call.data == "answer7_question8_btn2":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['ivt'] += 1
        user_id[user_id_key]['ping'] += 1
        user_id[user_id_key]['pinf'] += 1
        user_id[user_id_key]['moiais'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer8_question9_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer8_question9_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer8_question9_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer8_question9_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer8_question9_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer8_question9_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer8_question9_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer8_question9_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer8_question9_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[7]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[8], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer7_question8_btn3":

        user_id[user_id_key]['uvts'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer8_question9_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer8_question9_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer8_question9_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer8_question9_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer8_question9_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer8_question9_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer8_question9_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer8_question9_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer8_question9_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[7]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[8], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso

    if call.data == "answer7_question8_btn4":

        user_id[user_id_key]['i'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer8_question9_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer8_question9_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer8_question9_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer8_question9_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer8_question9_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer8_question9_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer8_question9_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer8_question9_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer8_question9_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[7]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[8], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso         

    if call.data == "answer7_question8_btn5":

        user_id[user_id_key]['bi'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer8_question9_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer8_question9_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer8_question9_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer8_question9_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer8_question9_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer8_question9_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer8_question9_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer8_question9_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer8_question9_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[7]+'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[8], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

             

# question 9
    if call.data == "answer8_question9_btn1":

        user_id[user_id_key]['ist'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer9_question10_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer9_question10_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer9_question10_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer9_question10_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer9_question10_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer9_question10_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer9_question10_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer9_question10_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer9_question10_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[8]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[9], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  
    
    if call.data == "answer8_question9_btn2":

        user_id[user_id_key]['pinf'] += 1
        user_id[user_id_key]['moiais'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer9_question10_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer9_question10_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer9_question10_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer9_question10_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer9_question10_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer9_question10_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer9_question10_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer9_question10_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer9_question10_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[8]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[9], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer8_question9_btn3":

        user_id[user_id_key]['ping'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer9_question10_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer9_question10_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer9_question10_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer9_question10_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer9_question10_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer9_question10_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer9_question10_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer9_question10_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer9_question10_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[8]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[9], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso

    if call.data == "answer8_question9_btn4":

        user_id[user_id_key]['i'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer9_question10_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer9_question10_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer9_question10_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer9_question10_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer9_question10_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer9_question10_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer9_question10_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer9_question10_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer9_question10_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[8]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[9], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso         

    if call.data == "answer8_question9_btn5":

        user_id[user_id_key]['rso'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer9_question10_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer9_question10_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer9_question10_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer9_question10_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer9_question10_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer9_question10_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer9_question10_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer9_question10_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer9_question10_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[8]+'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[9], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer8_question9_btn6":

        user_id[user_id_key]['bi'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer9_question10_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer9_question10_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer9_question10_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer9_question10_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer9_question10_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer9_question10_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer9_question10_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer9_question10_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer9_question10_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[8]+'Вы выбрали *вариант 6*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[9], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer8_question9_btn7":

        user_id[user_id_key]['moiais'] += 1
    

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer9_question10_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer9_question10_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer9_question10_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer9_question10_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer9_question10_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer9_question10_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer9_question10_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer9_question10_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer9_question10_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[8]+'Вы выбрали *вариант 7*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[9], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso            

# question 9
    if call.data == "answer9_question10_btn1":

        user_id[user_id_key]['ist'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer9_question10_btn2":

        user_id[user_id_key]['moiais'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso

    if call.data == "answer9_question10_btn3":

        user_id[user_id_key]['ivt'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer9_question10_btn4":

        user_id[user_id_key]['ping'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso    

    if call.data == "answer9_question10_btn5":

        user_id[user_id_key]['uvts'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso    

    if call.data == "answer9_question10_btn6":

        user_id[user_id_key]['pinf'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 6*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer9_question10_btn7":

        user_id[user_id_key]['i'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 7*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer9_question10_btn8":

        user_id[user_id_key]['bi'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 8*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso 

    if call.data == "answer9_question10_btn9":

        user_id[user_id_key]['rso'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer10_question11_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer10_question11_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer10_question11_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer10_question11_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer10_question11_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer10_question11_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer10_question11_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer10_question11_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer10_question11_btn9')
        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[9] + 'Вы выбрали *вариант 9*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[10], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso                           

# question 10
    if call.data == "answer10_question11_btn1":

        user_id[user_id_key]['moiais'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer11_question12_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer11_question12_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer11_question12_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer11_question12_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer11_question12_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer11_question12_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer11_question12_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer11_question12_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer11_question12_btn9')
        keyboard.add(btn1, btn2, btn3, btn4)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[10]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[11], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)             
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer10_question11_btn2":

        user_id[user_id_key]['ist'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer11_question12_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer11_question12_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer11_question12_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer11_question12_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer11_question12_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer11_question12_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer11_question12_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer11_question12_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer11_question12_btn9')
        keyboard.add(btn1, btn2, btn3, btn4)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[10]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[11], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)             
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso      

    if call.data == "answer10_question11_btn3":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['ivt'] += 1

        user_id[user_id_key]['ping'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer11_question12_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer11_question12_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer11_question12_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer11_question12_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer11_question12_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer11_question12_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer11_question12_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer11_question12_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer11_question12_btn9')
        keyboard.add(btn1, btn2, btn3, btn4)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[10]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[11], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)             
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso  

    if call.data == "answer10_question11_btn4":

        user_id[user_id_key]['uvts'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer11_question12_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer11_question12_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer11_question12_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer11_question12_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer11_question12_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer11_question12_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer11_question12_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer11_question12_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer11_question12_btn9')
        keyboard.add(btn1, btn2, btn3, btn4)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[10]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[11], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)             
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   

    if call.data == "answer10_question11_btn5":

        user_id[user_id_key]['pinf'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer11_question12_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer11_question12_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer11_question12_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer11_question12_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer11_question12_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer11_question12_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer11_question12_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer11_question12_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer11_question12_btn9')
        keyboard.add(btn1, btn2, btn3, btn4)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[10]+'Вы выбрали *вариант 5*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[11], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)             
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   

    if call.data == "answer10_question11_btn6":

        user_id[user_id_key]['i'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer11_question12_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer11_question12_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer11_question12_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer11_question12_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer11_question12_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer11_question12_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer11_question12_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer11_question12_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer11_question12_btn9')
        keyboard.add(btn1, btn2, btn3, btn4)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[10]+'Вы выбрали *вариант 6*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[11], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)             
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso   

    if call.data == "answer10_question11_btn7":

        user_id[user_id_key]['bi'] += 1
        user_id[user_id_key]['ist'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer11_question12_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer11_question12_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer11_question12_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer11_question12_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer11_question12_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer11_question12_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer11_question12_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer11_question12_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer11_question12_btn9')
        keyboard.add(btn1, btn2, btn3, btn4)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[10]+'Вы выбрали *вариант 7*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[11], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)             
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso 

    if call.data == "answer10_question11_btn8":

        user_id[user_id_key]['rso'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='answer11_question12_btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer11_question12_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer11_question12_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer11_question12_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer11_question12_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer11_question12_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer11_question12_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer11_question12_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer11_question12_btn9')
        keyboard.add(btn1, btn2, btn3, btn4)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[10]+'Вы выбрали *вариант 8*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[11], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)             
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso                  

    if call.data == "answer11_question12_btn1":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['ivt'] += 1
        user_id[user_id_key]['ping'] += 1
        user_id[user_id_key]['pinf'] += 1

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Посмотреть результат', callback_data='result')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[11]+'Вы выбрали *вариант 1*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[12], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso

    if call.data == "answer11_question12_btn2":

        user_id[user_id_key]['ist'] += 1
        user_id[user_id_key]['moiais'] += 1
       

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Посмотреть результат', callback_data='result')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[11]+'Вы выбрали *вариант 2*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[12], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso    

    if call.data == "answer11_question12_btn3":

        user_id[user_id_key]['uvts'] += 1
        user_id[user_id_key]['i'] += 1
        user_id[user_id_key]['bi'] += 1
      

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Посмотреть результат', callback_data='result')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[11]+'Вы выбрали *вариант 3*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[12], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso
         
    if call.data == "answer11_question12_btn4":

        user_id[user_id_key]['rso'] += 1
        

        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Посмотреть результат', callback_data='result')
        btn2 = types.InlineKeyboardButton('2', callback_data='answer2_question3_btn2')
        btn3 = types.InlineKeyboardButton('3', callback_data='answer2_question3_btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='answer2_question3_btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='answer2_question3_btn5')
        btn6 = types.InlineKeyboardButton('6', callback_data='answer2_question3_btn6')
        btn7 = types.InlineKeyboardButton('7', callback_data='answer2_question3_btn7')
        btn8 = types.InlineKeyboardButton('8', callback_data='answer2_question3_btn8')
        btn9 = types.InlineKeyboardButton('9', callback_data='answer2_question3_btn9')
        keyboard.add(btn1)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[11]+'Вы выбрали *вариант 4*', parse_mode='Markdown') 
        bot.send_message(call.message.chat.id, infa.question[12], reply_markup=keyboard, parse_mode='Markdown')  
        print( user_id)
        return ist, moiais, ivt, ping, uvts, pinf, i, bi, rso

    if call.data == "result":

      
        # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        

        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[13], parse_mode='Markdown') 
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEBzDJgCTg1CIfXPah_C-TEo010xNw1dQACXwAD29t-AAGEsFSbEa7K4x4E')

        bot.send_message(call.message.chat.id, infa.question[13], parse_mode='Markdown')  
        print( user_id)

        time.sleep(5)
        
        survey_list = [('09.03.02 - Информационные системы и технологии', user_id[user_id_key]['ist']),
         ('02.03.03 - Математическое обеспечение и администрирование информационных систем', user_id[user_id_key]['moiais']),
         ('09.03.01 - Информатика и вычислительная техника', user_id[user_id_key]['ivt']),
         ('09.03.04 - Программная инженерия', user_id[user_id_key]['ping']),
         ('27.03.04 - Управление в технических системах', user_id[user_id_key]['uvts']),
         ('09.03.03 - Прикладная информатика', user_id[user_id_key]['pinf']),
         ('27.03.05 - Инноватика', user_id[user_id_key]['i']),
         ('38.03.05 - Бизнес-информатика', user_id[user_id_key]['bi']),
         ('42.03.01 - Реклама и связи с общественностью', user_id[user_id_key]['rso'])]
        list_s= sorted(survey_list, key=itemgetter(1), reverse= True)
        print(list_s)
        survey_dict=dict(list_s)
        list_survey=list(survey_dict.keys())
        list_points=list(survey_dict.values())
        s= sum(list_points)
        print(sum(list_points))
        r = str(round(100/s*list_points[0], 1))
        r1 = str(round(100/s*list_points[1], 1))
        r2 = str(round(100/s*list_points[2], 1))
        
        print(list_survey[0])

        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=infa.question[1], parse_mode='Markdown') 
       
        bot.send_message(call.message.chat.id, infa.question[14], parse_mode='Markdown')  
        bot.send_message(call.message.chat.id,
         '\U0001F539'+list_survey[0]+' - '+r+'%'+'\n\U0001F539'+list_survey[1]+' - '+r1+'%'+'\n\U0001F539'+list_survey[2]+' - '+r2+'%',  parse_mode='Markdown')  
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEBzE1gCVxfY3Jz-7iJMegPt_7ETDhvQQACPwAD29t-AAH05pw4AeSqaR4E')
        
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Направления подготовки', callback_data='training')
        btn2 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
        
        keyboard.add(btn1)

        keyboard.add(btn2)

        

        bot.send_message(call.message.chat.id, infa.question[15], reply_markup=keyboard ,parse_mode='Markdown') 


            

   

   
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Главное меню бота\U0001F916':
        
        # survey_list = [('1', exz1), ('2', exz2), ('3', exz3)]
        # list_s= sorted(survey_list, key=itemgetter(1), reverse= True)
        # print(list_s)
        # survey_dict=dict(list_s)
        # list_survey=list(survey_dict.keys())
        # list_points=list(survey_dict.values())
        # print(list_survey[0])
        
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="О ФИСТ", callback_data="o_fist")
        btn2 = types.InlineKeyboardButton(text="Кафедры", callback_data="deportment")
        btn3 = types.InlineKeyboardButton(text="Пройти опрос", callback_data="survey_ekz")
        btn4 = types.InlineKeyboardButton(text="Показать на карте", callback_data="location")
        btn5 = types.InlineKeyboardButton(text="Контакты", callback_data="contacts")
        btn6 = types.InlineKeyboardButton(text="Полезные ссылки", callback_data="links")
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        keyboard.add(btn5)
        keyboard.add(btn6)
        # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANzX8qB2yAi_MNdJ-DPXO_nVk23iC8AAm8AA9vbfgABmVtQqHuTgHQeBA')
        bot.send_message(message.chat.id, '*Главное меню:*', reply_markup=keyboard, parse_mode='Markdown')
    
    else:
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
        # btn2 = types.InlineKeyboardButton('<', callback_data='kaf6')
        # btn3 = types.InlineKeyboardButton('Контакты', callback_data='deportment_contacts4')
        keyboard.add(btn1)
        # keyboard.add(btn3)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICEV_N_n92vOYl3ZJEB5vYj4npb9cMAAJjAAPb234AAYydBT3nQoPnHgQ')
        bot.send_message(message.chat.id, 'Я не понимаю... \nНажми кнопку ниже\U0001F447', reply_markup=keyboard, parse_mode='Markdown')  
    
#     if call.data == "pwd3":
#         keyboard = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton('Перегенирировать', callback_data='pwd3')
#         btn2 = types.InlineKeyboardButton('Вернутся в начало', callback_data='start')
#         keyboard.add(btn1)
#         keyboard.add(btn2)
#         pwd = password_generate.hard_pass(config.pwd_length)
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твой пароль - `{0}`".format(pwd), reply_markup=keyboard, parse_mode='Markdown')

# @bot.message_handler(content_types=['sticker'])
# def i(message):
# 	print(message)


# @bot.message_handler(commands=["start"])
# def inline(message):
#   key = types.InlineKeyboardMarkup()
#   but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
#   but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
#   but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
#   key.add(but_1, but_2, but_3)
#   # bot.send_message(message.chat.id, "ВЫБЕРИТЕ КНОПКУ", reply_markup=key)

#   bot.send_photo(message.chat.id, 'https://i.ytimg.com/vi/jhFsFZXZbu4/maxresdefault.jpg', caption= "ВЫБЕРИТЕ КНОПКУ", reply_markup=key) # picture
#   bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANXX8p2U59fl_PRDrklkgxjggABozyRAALCAAOWn4wOOwsHDxoBJlgeBA')

# @bot.callback_query_handler(func=lambda c:True)
# def inline(c):
#   if c.data == 'NumberOne':
#     bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=infa.m + "1", parse_mode='Markdown')

#   if c.data == 'NumberTwo':
#     bot.send_message(c.message.chat.id, 'Это кнопка 2')
#   if c.data == 'NumberTree':
#     key = types.InlineKeyboardMarkup()
#     but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
#     but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
#     but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
#     key.add(but_1, but_2, but_3)
#     bot.send_message(c.message.chat.id, 'Это кнопка 3', reply_markup=key)

  

bot.polling(none_stop=True, interval=0)
# if __name__ == '__main__':
#     bot.skip_pending = True
#     # bot.polling(none_stop=True, interval=2)
#     bot.infinity_polling(True)



# while True:
#     try:
#         bot.polling(none_stop=True)

#     except Exception as e:
#         print(e)  # или просто print(e) если у вас логгера нет,
#         # или import traceback; traceback.print_exc() для печати полной инфы
#         time.sleep(15)    