from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.i18n import I18n

from settings import LINK_TO_REPO


def keyboard(_: I18n.gettext) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_('My repository on GitHub.'), url=LINK_TO_REPO)
            ],
        ]
    )
    return markup
