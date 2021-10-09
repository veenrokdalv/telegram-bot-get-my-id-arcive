from aiogram import Dispatcher

from . import message, service_messages


def setup(dispatcher: Dispatcher):
    for module in (message, service_messages):
        module.setup(dispatcher)
