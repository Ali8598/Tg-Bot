from decouple import config
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


Tk=config('token')

# پیکربندی لاگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# تابع start
async def start(update: Update, context: CallbackContext) -> None:
    # این تابع دکمه‌ها را برای کاربر می‌سازد
    keyboard = [
        [InlineKeyboardButton("فهرست اصلی", callback_data='main')],
        [InlineKeyboardButton("دکمه 1", callback_data='button1')],
        [InlineKeyboardButton("دکمه 2", callback_data='button2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text('سلام! برای انتخاب یک گزینه، موضوع مورد نظر را انتخاب کنید:', reply_markup=reply_markup)
    
    
    # await update.message.reply_text('صلی الله علیک یا بقیه الله')
    # await update.message.reply_text('سلام!')
    
    #این تابع برای مدیریت زیرمجموعه‌ها است
async def button(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'main':
        keyboard = [
            [InlineKeyboardButton("روایـــات", callback_data='sub1')],
            [InlineKeyboardButton("شبهــــات", callback_data='sub2')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="شما در فهرست اصلی هستید. انتخاب کنید:", reply_markup=reply_markup)
    
    elif query.data == 'sub1':
        await query.edit_message_text(text="شما زیرمجموعه روایات را انتخاب کردید.")
    
    elif query.data == 'sub2':
        await query.edit_message_text(text="شما زیرمجموعه شبهات را انتخاب کردید.")
    
    else:
        await query.edit_message_text(text=f"شما {query.data} را انتخاب کردید.")

# تابع اصلی
def main():
    #Token='7775167556:AAE8uW2mkR8KIAco9PkjEA3k5_6I1vI3vnk'
    application = Application.builder().token(Tk).build()

    # اضافه کردن هندلر برای فرمان /start
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    logger.info("Robot start...")

    # شروع دریافت پیام‌ها و پاسخ به آن‌ها
    application.run_polling()

if __name__ == '__main__':
    main()
    
    
    
