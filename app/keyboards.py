from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start_btn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Руссский язык', callback_data='select_ru')],[InlineKeyboardButton(text='Қазақ тілі', callback_data='select_kz')]])

website_link_btn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти на сайт", url="https://r2p.kz/")],  [InlineKeyboardButton(text='Назад', callback_data="back_btn_ru")]])

payment_link_btn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Перейти к оплате', url='https://r2p.kz/#Pay')], [InlineKeyboardButton(text='Назад', callback_data="back_btn_ru")]])

cons_help_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data='back_btn_ru')]])

back_btn_ru = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data='back_btn_ru')]])

async def list_of_sections():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='Способы оплаты', callback_data='btn_payment'),
        InlineKeyboardButton(text='Информация о компании', callback_data='btn_info'),
        InlineKeyboardButton(text='Помощь консультанта', callback_data='btn_cons_help'),
        InlineKeyboardButton(text="Смена языка", callback_data='change_language'),
    )
    return keyboard.adjust(2, 1).as_markup()
