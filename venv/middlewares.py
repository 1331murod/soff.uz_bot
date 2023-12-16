from aiogram import BaseMiddleware
from aiogram.types import Message


class CheckUserMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.re

    async def __call__(self, handler, event, data):
        self.counter += 1
        data['counter'] = self.counter
        return await handler(event, data)
    

router = Router()
router.message.middleware(CounterMiddleware())