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
            f'Welcome, {html.quote(message.from_user.full_name)}! {html.link("My repo", LINK_TO_REPO)}!\n'
            f'My username - @{bot_me.username}\n'
            f'Use the /help command to familiarize yourself with me.\n\n'
            f'<i>Your account ID:</i> {html.code(message.from_user.id)}\n'
            f'<i>Your account username:</i> {formatting.username(user_username=message.from_user.username, default="-")}\n'
        ),
        reply_markup=inline.link_to_repo.keyboard(_),
        disable_web_page_preview=True,
    )


def setup(dispatcher: Dispatcher):
    dispatcher.message.register(
        start, state=None, commands=['start'], chat_type='private', is_forwarded=False,
    )
