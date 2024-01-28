from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message
from conf import * 
from keyboards.base import based

class CheckSubscription(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member("@tyan_corp", event.from_user.id)

        if chat_member.status == "left":
            await event.answer_animation(bf, caption="<i>Подпишишь скорее на канал, а потом я буду вся твоя</i>", 
    reply_markup=based())
        else:
            return await handler(event, data)