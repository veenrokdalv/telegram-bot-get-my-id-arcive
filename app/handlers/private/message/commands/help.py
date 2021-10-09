from aiogram import Dispatcher, html
from aiogram.types import Message
from aiogram.utils.i18n import I18n

from app.keyboards import inline

__all__ = ['setup']

from settings import LINK_TO_REPO


async def help_menu(message: Message, _: I18n.gettext):
    await message.answer(
        text=_(
            f'My commands.\n'
            f'/start - <b>Start bot.</>\n'
            f'/help - <b>Help menu.</>\n'
            f'/getchatid - <b>Give current chat ID.</>\n'
            f'/getmyid - <b>Give Your account ID.</>\n\n'
            'This bot allows you to find out the user ID, message or chat. '
            'Add the bot to the chat and use the /getmyid or /getchatid command to find out '
            '<b>Your ID</> or <b>Chat ID</>, respectively.\n'
            'You can also write in private messages to the bot to find out '
            '<b>Your ID</> or forward a message to <b>Another user</> and get information about him.\n\n'
            f'{html.link("My repository on github", LINK_TO_REPO)}.'
        ),
        reply_markup=inline.link_to_repo.keyboard(_),
        disable_web_page_preview=True,

    )


def setup(dispatcher: Dispatcher):
    dispatcher.message.register(
        help_menu, state=None, commands=['help'], chat_type='private',
    )
