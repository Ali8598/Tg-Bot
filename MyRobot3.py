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
        [InlineKeyboardButton("فهرست اصلی موضوعات", callback_data='subjects')],
        [InlineKeyboardButton("روایـــات", callback_data='revayat')],
        [InlineKeyboardButton("شبهــــات", callback_data='shobahat')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text('سلام! برای انتخاب یک گزینه، موضوع مورد نظر را انتخاب کنید:', reply_markup=reply_markup)
    
    
    # await update.message.reply_text('صلی الله علیک یا بقیه الله')
    # await update.message.reply_text('سلام!')
    
    #این تابع برای مدیریت زیرمجموعه‌ها است
async def button(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'subjects':
        keyboard = [
            [InlineKeyboardButton("وصیـــت", callback_data='vaseyat')],
            [InlineKeyboardButton("خواب و رویــا", callback_data='khaab')],
            [InlineKeyboardButton("تکلم به تمام زبانها", callback_data='takalom')],
            [InlineKeyboardButton("12 امام و 14 معصوم", callback_data='12emam')],
            [InlineKeyboardButton("بازگشت به فهرست اصلی", callback_data='back_to_main')],
            
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="شما در فهرست اصلی هستید. انتخاب کنید:", reply_markup=reply_markup)
    
    elif query.data == 'revayat':
        keyboard = [
            [InlineKeyboardButton("صحیح السند", callback_data='sahih')],
            [InlineKeyboardButton("متواتر", callback_data='motavater')],
            [InlineKeyboardButton("ضعیـف السند", callback_data='zaeif')],
            [InlineKeyboardButton("بازگشت به فهرست اصلی", callback_data='back_to_main')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="شما زیرمجموعه روایات را انتخاب کردید.", reply_markup=reply_markup)
    
    elif query.data == 'shobahat':
        keyboard = [
            [InlineKeyboardButton("سیزده امام", callback_data='13emam')],
            [InlineKeyboardButton("مردی قبل از مهدی (ع)", callback_data='mardi')],
            [InlineKeyboardButton("شبهه رفع", callback_data='rofe')],
            [InlineKeyboardButton("مهدیـین", callback_data='mahdein')],
            [InlineKeyboardButton("بازگشت به فهرست اصلی", callback_data='back_to_main')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="شما زیرمجموعه شبهات را انتخاب کردید.", reply_markup=reply_markup)
    # # نمایش پیام برای هر انتخاب دیگر
    # elif query.data.startswith('sub1') or query.data.startswith('sub2'):
    #     await query.edit_message_text(text=f"شما {query.data} را انتخاب کردید.")
        
        
    elif query.data == 'back_to_main':
        keyboard = [
            [InlineKeyboardButton("فهرست اصلی موضوعات", callback_data='subjects')],
            [InlineKeyboardButton("روایـــات", callback_data='revayat')],
            [InlineKeyboardButton("شبهــــات", callback_data='shobahat')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="شما در فهرست اصلی هستید. انتخاب کنید:", reply_markup=reply_markup)
        
    # زیرمنو 2-1 (نمایش متن مرتبط با زیرمنو 2-1)
    
    
    elif query.data == 'sahih':
        t1 = """
#ایه_نریدان_نمن_علی_الذین_استضعفوا


عَنِ الْمُفَضَّلِ بْنِ عُمَرَ قَالَ سَمِعْتُ أَبَا عَبْدِ اللَّهِ ع يَقُولُ‏:
 إِنَّ رَسُولَ اللَّهِ ص نَظَرَ إِلَى عَلِيٍّ وَ الْحَسَنِ وَ الْحُسَيْنِ ع فَبَكَى وَ قَالَ:
 أَنْتُمُ الْمُسْتَضْعَفُونَ بَعْدِي
 قَالَ الْمُفَضَّلُ فَقُلْتُ لَهُ مَا مَعْنَى ذَلِكَ يَا ابْنَ رَسُولِ اللَّهِ 
قَالَ مَعْنَاهُ أَنَّكُمُ الْأَئِمَّةُ بَعْدِي
 إِنَّ اللَّهَ عَزَّ وَ جَلَّ يَقُولُ: "وَ نُرِيدُ أَنْ نَمُنَّ عَلَى الَّذِينَ اسْتُضْعِفُوا فِي الْأَرْضِ وَ نَجْعَلَهُمْ أَئِمَّةً وَ نَجْعَلَهُمُ‏ الْوارِثِينَ‏" فَهَذِهِ الْآيَةُ جَارِيَةٌ فِينَا إِلَى يَوْمِ الْقِيَامَةِ».
📚 معاني الأخبار ص79
🎋🍃🎋🍃🎋🍃🎋🍃🎋🍃
مفضّل بن عمر گويد:
از امام صادق عليه السلام شنيدم كه فرمود:
رسول خدا صلى اللّٰه عليه و آله نظرى به علىّ‌ و حسن و حسين افكند و گريست و فرمود:
شما مستضعفان بعد از وفات من هستيد.
مفضّل گويد:عرض كردم يا ابن رسول اللّٰه معنى آن چيست‌؟
فرمود:يعنى شما امامان بعد از من هستيد.
چون خداوند مى‌فرمايد:
«وَ نُرِيدُ أَنْ‌ نَمُنَّ‌ عَلَى اَلَّذِينَ‌ اُسْتُضْعِفُوا فِي اَلْأَرْضِ‌ وَ نَجْعَلَهُمْ‌ أَئِمَّةً‌ وَ نَجْعَلَهُمُ‌ اَلْوٰارِثِينَ‌ »
(و مى‌خواهيم بر آنان كه در زمين خوار و زبون گرفته شده‌اند تفضّل نمائيم،و آنان را پيشوايان گردانيم،و نيز وارث حكومت حقّ‌ سازيم) این آیه تا روز قیامت در مورد ما جاریست."""
        await query.edit_message_text(text= t1) 
        

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
    
    
    
