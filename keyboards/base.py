from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def getin() -> InlineKeyboardMarkup:
    bld = InlineKeyboardBuilder()
    bld.row(InlineKeyboardButton(text="Подписаться", url="https://t.me/tyan_corp"))
    bld.row(InlineKeyboardButton(text="Проверить", callback_data="check"))
    
    return bld.as_markup()