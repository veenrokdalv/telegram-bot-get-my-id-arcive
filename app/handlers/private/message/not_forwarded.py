from aiogram import Dispatcher, html

from aiogram.types import Message
from aiogram.utils.i18n import I18n

__all__ = ['setup']


async def send_info_from_message(message: Message, _: I18n.gettext):
    await message.answer(
        text=_(
            '<i>Your account ID:</i> <code>{user_account_id}</>\n'
        ).format(
            user_account_id=message.from_user.id
        )
    )


def setup(dispatcher: Dispatcher, *args, **kwargs):
    dispatcher.message.register(
        send_info_from_message, chat_type='private', is_forwarded=False,
    )
