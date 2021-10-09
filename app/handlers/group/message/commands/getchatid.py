from aiogram import Dispatcher, html

from aiogram.types import Message
from aiogram.utils.i18n import I18n

__all__ = ['setup']


async def send_info_from_message(message: Message, _: I18n.gettext):
    await message.answer(
        text=_(
            '<i>Your account ID:</i> <code>{user_account_id}</>\n'
            '<i>Current chat ID:</i> <code>{current_chat_id}</>\n'
            '<i>Current message ID:</i> <code>{current_message_id}</>\n'
        ).foramt(
            user_account_id=message.from_user.id,
            current_chat_id=message.chat.id,
            current_message_id=message.message_id
        )
    )


def setup(dispatcher: Dispatcher, *args, **kwargs):
    dispatcher.message.register(
        send_info_from_message, commands=['getchatid'], chat_type=['group', 'supergroup'], is_forwarded=False,
    )
