from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
import logging
from app.ai_model import recognize

router = Router()

@router.message(CommandStart())
async def handle_start(message: Message):
    await send_welcome_message(message)

async def send_welcome_message(message: Message):
    if message.from_user.last_name is None:
        await message.answer_photo(
            photo='AgACAgIAAxkBAAIG_ma3Rjdt6I-5cx7qEwcoRugu8HM2AALN3zEbW8bASTc5LhqdFbTIAQADAgADbQADNQQ',
            caption=f'Здравствуйте {message.from_user.first_name}, вас приветствует бот Мадина. Я помогу вам получить нужную вам информацию по вашему делу или по состоянию договора.\n'
                    f'Сәлеметсіз бе, {message.from_user.first_name}! Менің есімім Мадина. Мен сізге қажетті ақпаратты алу немесе келісімшарттар жағдайы бойынша көмек көрсетемін.\n'
        )
    else:
        await message.answer_photo(
            photo='AgACAgIAAxkBAAIG_ma3Rjdt6I-5cx7qEwcoRugu8HM2AALN3zEbW8bASTc5LhqdFbTIAQADAgADbQADNQQ',
            caption=f'Здравствуйте {message.from_user.first_name} {message.from_user.last_name}, вас приветствует бот Мадина. Я помогу вам получить нужную вам информацию по вашему делу или по состоянию договора.\n'
                    f'Сәлеметсіз бе, {message.from_user.first_name} {message.from_user.last_name}! Менің есімім Мадина. Мен сізге қажетті ақпаратты алу немесе келісімшарттар жағдайы бойынша көмек көрсетемін.\n'
        )
    await message.answer(
        text=f'Для выбора языка используйте кнопки ниже.\n'
             f'Тіл таңдау үшін төмендегі батырмаларды пайдаланыңыз.\n',
        reply_markup=kb.start_btn
    )

@router.callback_query(F.data == 'change_language')
async def handle_change_language(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        text= f'Для выбора языка используйте кнопки ниже.\n'
              f'Тіл таңдау үшін төмендегі батырмаларды пайдаланыңыз.\n',
        reply_markup=kb.start_btn
    )

@router.callback_query(F.data.in_(['select_ru', 'back_btn_ru']))
async def sections_sheet(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Для продолжения, пожалуйста выберите необходимый раздел.', reply_markup=await kb.list_of_sections())

@router.callback_query(F.data == 'btn_info')
async def get_info(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'ТОО «Специальная финансовая компания «р2п инвест КЗ» создана в соответствии Законом Республики Казахстан "О проектном финансировании и секьюритизации". Предметом деятельности общества является приобретение прав требования к заемщикам об уплате денежных средств по кредитным договорам, договорам займа и (или) иным обязательствам.', reply_markup=kb.website_link_btn)

@router.callback_query(F.data == "btn_payment")
async def get_payment(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f"Раздел оплаты:\n"
                                  f"Для получения подробной информации о способах оплаты и состоянии задолженности нажмите <b>Перейти к оплате</b>.\n"
                                  f"Для возвращения в главное меню нажмите Назад\n", reply_markup=kb.payment_link_btn, parse_mode='HTML')

@router.callback_query(F.data == "btn_cons_help")
async def get_cons_help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f"Теперь вы общаетесь с ИИ-консультантом. Напишите свой вопрос.", reply_markup=kb.cons_help_menu)

@router.message(F.text)
async def handle_message(message: Message):
    user_text = message.text
    response = recognize(user_text)
    await message.answer(response)


