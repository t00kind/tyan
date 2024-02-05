from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from database import get_all
def based() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Подписаться 🔗", url="https://t.me/tyan_corp"))
    kb.row(InlineKeyboardButton(text="Проверить ✅", callback_data="check"))
    return kb.as_markup()

def true() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Найти 🔎", callback_data="find"))
    return kb.as_markup()
def false() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Показать", callback_data="find"))
    return kb.as_markup()

def hash() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Добавить аниме", callback_data="add"))
    kb.row(InlineKeyboardButton(text="Сменить режим", callback_data="switch"))
    kb.row(InlineKeyboardButton(text="Общий список", callback_data="pop"))
    return kb.as_markup()

def magic(link) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Смотреть у нас", url=link))
    
    return kb.as_markup()
def bash() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Я 9 из Хокаге 🌀, как Наруто Узумаки ", callback_data="dream"))
    return kb.as_markup()