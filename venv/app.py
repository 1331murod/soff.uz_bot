from aiogram import Bot, Dispatcher,types
from aiogram.utils import executor
from states import *
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from integrations import get_refferall


storage = MemoryStorage()

BOT_TOKEN ='6761168993:AAEILVR-fglJSy_3UqVA1-irHiE9jIQ9b_g'

class Profile(StatesGroup):
    username = State()
    password = State()

async def checkmember(user_id):
    channels = ['@nimadur_UZ',]
    for chat_username in channels:
        try:
            member =await bot.get_chat_member(chat_username, user_id)
            status = member.status
            a = status in ('member', 'creator', 'administrator')
            if not a:
                return False
        except Exception as e:
            print(f"Xato yuz berdi: {e}")
            return False
    return True


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

def chanels_buttons() -> types.InlineKeyboardMarkup:
    ink = types.InlineKeyboardMarkup(row_width=2)
    tg_url = types.InlineKeyboardButton('Telegram Kanalimiz', url='https://t.me/nimadur_UZ')
    ink.add(tg_url)
    return ink


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    reply = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("/register")
    reply.add(button)
    if not await checkmember(message.from_user.id):
        return await message.answer(text="Bu botdan foydalanish uchun quyidagi kanalga a'zo boling", reply_markup=chanels_buttons())
        
    await message.answer(text="Referall link olishingiz uchun ro'yhatdan o'ting", reply_markup=reply )



@dp.message_handler(commands=['register'])
async def start_login(message: types.Message):
    await message.answer("Tizimda ro'yhatdan o'tgan telefon raqam yo'ki email ingizni kiriting ")
    await Profile.username.set()
    

@dp.message_handler(state=Profile.username)
async def set_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("parolni kiriting")
    await Profile.password.set()


@dp.message_handler(state=Profile.password)
async def set_password(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    response = get_refferall(data['username'], data['password'])
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True,)
