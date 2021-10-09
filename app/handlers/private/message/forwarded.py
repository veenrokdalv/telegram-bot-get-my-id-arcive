from aiogram import Dispatcher, html

from aiogram.types import Message
from aiogram.utils.i18n import I18n

__all__ = ['setup']


async def send_info_from_message(message: Message, _: I18n.gettext):
    forward_from = message.forward_from
    forward_from_chat = message.forward_from_chat
    forward_from_message_id = message.forward_from_message_id

    if forward_from:
        forward_from_info = _(
            '<i>Forward from account ID:</i> <code>{forward_from_id}</>\n'
        ).format(forward_from_id=html.code(forward_from and forward_from.id or "-"))
    else:
        forward_from_info = ''

    if forward_from_chat or forward_from_message_id:
        forward_from_chat_info = _(
            '<i>Forward from chat ID:</i> <code>{forward_from_chat_id}</>\n'
            '<i>Forward from message ID:</i> <code>{forward_from_message_id}</>\n'
        ).format(
            forward_from_chat_id=forward_from_chat and forward_from_chat.id or "-",
            forward_from_message_id=forward_from_message_id or "-"
        )
    else:
        forward_from_chat_info = ''

    await message.answer(
        text=_(
            '<i>Your account ID:</i> <code>{user_account_id}</>\n'
            '{forward_from_info}'
            '{forward_from_chat_info}'
        ).format(
            forward_from_info=forward_from_info,
            forward_from_chat_info=forward_from_chat_info,
            user_account_id=message.from_user.id
        )
    )


def setup(dispatcher: Dispatcher, *args, **kwargs):
    dispatcher.message.register(
        send_info_from_message, chat_type='private', is_forwarded=True,
    )
