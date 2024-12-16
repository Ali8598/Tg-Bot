from decouple import config
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging


Tk=config('token')

# پیکربندی لاگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# تابع start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('صلی الله علیک یا بقیه الله')
    await update.message.reply_text('سلام!')
    

# تابع اصلی
def main():
    #Token='7775167556:AAE8uW2mkR8KIAco9PkjEA3k5_6I1vI3vnk'
    application = Application.builder().token(Tk).build()

    # اضافه کردن هندلر برای فرمان /start
    application.add_handler(CommandHandler("start", start))

    logger.info("Robot start...")

    # شروع دریافت پیام‌ها و پاسخ به آن‌ها
    application.run_polling()

if __name__ == '__main__':
    main()
    