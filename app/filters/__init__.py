from aiogram import Dispatcher

import loggers
from . import (translated_inline_query_text, translated_message_text, chat_type, message_is_forwarded)


def setup(dispatcher: Dispatcher):
    for module in (translated_inline_query_text, translated_message_text, chat_type, message_is_forwarded):
        module.setup(dispatcher)
    loggers.filters.debug('Setup filters.')
