from aiogram import Dispatcher, html
from aiogram.types import Message
from aiogram.utils.i18n import I18n

from app.utils.bot.send_keyboards import get_main_keyboard

__all__ = ['setup']

from settings import LINK_TO_REPO


async def help_menu(message: Message, _: I18n.gettext):
    await message.answer(
        reply_markup=get_main_keyboard(_, message.from_user),
        text=_(
            f'My commands.\n'
            f'/start\n'
            f'/help'
            f'/getchatid - Give current chat ID\n'
            f'/getmyid - Give Your account ID\n'
            'This bot allows you to find out the user ID, message or chat.'
            'Add the bot to the chat and use the /getmyid or /getchatid command to find out '
            'Your ID or Chat ID, respectively.'
            'You can also write in private messages to the bot to find out '
            'Your ID or forward a message to another user and get information about him.\n\n'
            f'{html.link("My repository on github", LINK_TO_REPO)}.'
        )
    )


def setup(dispatcher: Dispatcher):
    dispatcher.message.register(
        help_menu, state=None, commands=['help'], chat_type='private',
    )
