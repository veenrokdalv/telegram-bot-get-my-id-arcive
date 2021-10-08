from aiogram import Dispatcher, html
from aiogram.types import Message
from aiogram.utils.i18n import I18n

from app.utils.helper import formatting
from settings import LINK_TO_REPO


async def start(message: Message, _: I18n.gettext):

    await message.answer(
        text=_(
            f'Welcome, {html.quote(message.from_user.full_name)}! {html.link("My repo", LINK_TO_REPO)}!\n'
            f'<i>Your account ID:</i> {html.code(message.from_user.id)}\n'
            f'<i>Your account username:</i> {formatting.username(user_username=message.from_user.username, default="-")}\n'
        )
    )


def setup(dispatcher: Dispatcher):
    dispatcher.message.register(
        start, state=None, commands=['start'], chat_type='private', is_forwarded=False,
    )
