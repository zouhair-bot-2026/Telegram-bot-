import telebot
from telebot import types
import random
from datetime import datetime, timedelta

TOKEN = '8690998229:AAHgL0Roo7cW27-a5VD9bqgtdDmMkqVvGTk'
bot = telebot.TeleBot(TOKEN)

pairs = ['EUR/USD', 'GBP/USD', 'BTC/USD', 'XAU/USD', 'USD/JPY']
directions = ['BUY 🔼', 'SELL 🔽']

def generate_signal():
    pair = random.choice(pairs)
    direction = random.choice(directions)
    time_now = datetime.now().strftime("%H:%M")
    expiry = (datetime.now() + timedelta(minutes=5)).strftime("%H:%M")
    return f"📊 **إشارة جديدة**\n\nالزوج: `{pair}`\nالاتجاه: **{direction}**\nالدخول: الآن\nالصلاحية: {expiry}\n\n⚠️ تجريبية فقط"

@bot.message_handler(commands=['start', 'signal'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('🔄 إشارة أخرى', callback_data='new')
    markup.add(btn)
    bot.send_message(message.chat.id, generate_signal(), parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda c: True)
def callback(c):
    if c.data == 'new':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('🔄 إشارة أخرى', callback_data='new')
        markup.add(btn)
        bot.send_message(c.message.chat.id, generate_signal(), parse_mode='Markdown', reply_markup=markup)
        bot.answer_callback_query(c.id)

print("Bot started ✅")
bot.infinity_polling()
