from aiogram import Dispatcher

__all__ = ['setup']

from . import (start, help,)


def setup(dispatcher: Dispatcher, *args, **kwargs):
    for module in (start, help,):
        module.setup(dispatcher, *args, **kwargs)
