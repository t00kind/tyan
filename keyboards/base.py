from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def based() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Подписаться 🔗", url="https://t.me/tyan_corp"))
    kb.row(InlineKeyboardButton(text="Проверить ✅", callback_data="check"))
    return kb.as_markup()

def true() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Найти по коду 🔎", callback_data="find"))
    kb.row(InlineKeyboardButton(text="Показать список 🎇", callback_data="show"))
    return kb.as_markup()

def hash() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Добавить аниме", callback_data="add"))
    kb.row(InlineKeyboardButton(text="Сменить режим", callback_data="switch"))
    
    return kb.as_markup()
def bash() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Я 9 из Хокаге 🌀, как Наруто Узумаки ", callback_data="dream"))
    return kb.as_markup()