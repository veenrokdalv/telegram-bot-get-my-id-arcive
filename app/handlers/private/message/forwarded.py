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
            f'<i>Forward from account ID:</i> {html.code(forward_from and forward_from.id or "-")}\n'
        )
    else:
        forward_from_info = ''

    if forward_from_chat or forward_from_message_id:
        forward_from_chat_info = _(
            f'<i>Forward from chat ID:</i> {html.code(forward_from_chat and forward_from_chat.id or "-")}\n'
            f'<i>Forward from message ID:</i> {html.code(forward_from_message_id or "-")}\n'
        )
    else:
        forward_from_chat_info = ''

    await message.send_copy(message.from_user.id)
    await message.answer(
        text=_(
            f'<i>Your account ID:</i> {html.code(message.from_user.id)}\n'
            f'{forward_from_info if forward_from_info else ""}'
            f'{forward_from_chat_info if forward_from_chat_info else ""}'
        )
    )


def setup(dispatcher: Dispatcher, *args, **kwargs):
    dispatcher.message.register(
        send_info_from_message, chat_type='private', is_forwarded=True,
    )
