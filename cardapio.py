import telebot
import cardapio_ufscar
from datetime import datetime

################ API TOKEN ################
KEY = 'INSIRA O TOKEN DO SEU BOT AQUI'
bot = telebot.TeleBot(KEY)

@bot.message_handler(commands=['horario'])
def horario_local(session):
    horario = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    bot.send_message(chat_id=session.chat.id, text=horario)

@bot.message_handler(commands=['ru'])
def ru_ufscar(session):

    # Cardapio - proximo ru
    if session.text == '/ru':
        bot.send_message(chat_id=session.chat.id, text=cardapio_ufscar.msg(cardapio_ufscar.proximo()))

    # Cardapio - Amanha
    elif session.text == '/ru amanha':
        for item in cardapio_ufscar.amanha():
            bot.send_message(chat_id=session.chat.id, text=cardapio_ufscar.msg(item))
    
    # Cardapio - Hoje
    elif session.text == '/ru hoje':
        for item in cardapio_ufscar.hoje():
            bot.send_message(chat_id=session.chat.id, text=cardapio_ufscar.msg(item))
    
    # Cardapio - Almoco
    elif session.text == '/ru almoco':
        bot.send_message(chat_id=session.chat.id, text=cardapio_ufscar.msg(cardapio_ufscar.almoco()))
    
    # Cardapio - Jantar
    elif session.text == '/ru jantar':
        bot.send_message(chat_id=session.chat.id, text=cardapio_ufscar.msg(cardapio_ufscar.jantar()))


@bot.message_handler(commands=['help'])
def help_ufscar(session):
    # Ajuda - Lista os comandos do Bot
    if session.text == '/help':
        bot.send_message(chat_id=session.chat.id, text='/ru : mostra o próximo cardápio\n/ru amanha : mostra os cardápios(almoço e janta) de amanhã\n/ru hoje : mostra os cardápios(almoço e janta) de hoje\n/ru almoco : mostra o cardápio do almoço de hoje\n/ru jantar : mostra o cardápio da janta de hoje\n/horario : mostra o horario local\n')

bot.polling()

