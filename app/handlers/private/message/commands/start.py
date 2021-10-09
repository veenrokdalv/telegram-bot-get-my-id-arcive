from aiogram import Dispatcher, html, Bot
from aiogram.types import Message
from aiogram.utils.i18n import I18n

from app.keyboards import inline
from app.utils.helper import formatting
from settings import LINK_TO_REPO


async def start(message: Message, bot: Bot, _: I18n.gettext):
    bot_me = await bot.me()
    await message.answer(
        text=_(
            'Welcome, <b>{user_account_full_name}</>!\n'
            'My username - @{bot_me_username}\n'
            'Use the /help command to familiarize yourself with me.\n\n'
            '<i>Your account ID:</i> {user_account_id}\n'
            '<i>Your account username:</i> {user_account_username}\n'
        ).format(
            bot_me_username=bot_me.username,
            user_account_full_name=html.quote(message.from_user.full_name),
            user_account_id=html.code(message.from_user.id),
            user_account_username=formatting.username(user_username=message.from_user.username, default="-")
        ),
        reply_markup=inline.link_to_repo.keyboard(_),
        disable_web_page_preview=True,
    )


def setup(dispatcher: Dispatcher):
    dispatcher.message.register(
        start, state=None, commands=['start'], chat_type='private', is_forwarded=False,
    )
