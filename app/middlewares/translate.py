from typing import Any, Dict

from aiogram import Dispatcher
from aiogram.types import Update
from aiogram.utils.i18n import I18nMiddleware, I18n

from settings import DEFAULT_LOCALE

__all__ = ['setup']


class TranslationMiddleware(I18nMiddleware):

    def __init__(self, i18n: I18n):
        self.i18n = i18n

        super().__init__(i18n=self.i18n)

    async def get_locale(self, event: Update, data: Dict[str, Any]) -> str:
        event = event.event

        if hasattr(event, 'from_user'):
            return event.from_user.language_code

        return DEFAULT_LOCALE


def setup(dispatcher: Dispatcher, *args, **kwargs):
    i18n = kwargs['i18n']
    dispatcher.update.outer_middleware(TranslationMiddleware(i18n=i18n))
