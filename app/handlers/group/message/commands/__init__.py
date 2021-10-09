from aiogram import Dispatcher

from . import (getmyid, getchatid)

__all__ = ['setup']


def setup(dispatcher: Dispatcher, *args, **kwargs):
    for module in (getmyid, getchatid):
        module.setup(dispatcher, *args, **kwargs)
