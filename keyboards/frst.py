from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def based() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Подписаться 🔗", url="https://t.me/tyan_corp"))
    kb.row(InlineKeyboardButton(text="Проверить ✅", callback_data="check"))
    return kb.as_markup()

def true() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Найти По Коду")
    kb.button(text="Список")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)