import re
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

EMAIL_PATTERN = re.compile(
    r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

PHONE_PATTERN = re.compile ("^\+998[0-9]{9}")

class ProfileState(StatesGroup):
    user_id = State()
    
    phone = State()
    email = State()
    
storage = MemoryStorage()
