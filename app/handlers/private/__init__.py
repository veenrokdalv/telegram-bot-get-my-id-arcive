from aiogram import Dispatcher

from . import (message, )


def setup(dispatcher: Dispatcher):
    for module in (message, ):
        module.setup(dispatcher)
