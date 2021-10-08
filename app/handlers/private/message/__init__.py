from aiogram import Dispatcher

from . import commands, forwarded, not_forwarded

__all__ = ['setup']


def setup(dispatcher: Dispatcher, *args, **kwargs):
    for module in (commands, forwarded, not_forwarded):
        module.setup(dispatcher, *args, **kwargs)
