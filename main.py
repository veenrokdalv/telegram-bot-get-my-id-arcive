import datetime as dt
import logging
import os
from zoneinfo import ZoneInfo

from aiogram import Dispatcher, Bot, html
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher.fsm.strategy import FSMStrategy
from aiogram.utils.i18n import I18n
from sqlalchemy.ext.asyncio import AsyncEngine

import loggers
import settings
from app import middlewares, filters, handlers
from app.utils.bot import malling_message


async def _on_startup(bots: list[Bot], i18n: I18n, _: I18n.gettext):
    _start_time = settings.START_TIME.astimezone(ZoneInfo(settings.DEFAULT_TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")

    for bot in bots:
        bot_account = await bot.me()
        await malling_message.text(
            bot=bot, chat_ids=settings.SUPERUSERS_TELEGRAM_ID,
            message_text=_(
                'Bot started!\n'
                f'My id: {html.code(bot_account.id)}\n'
                f'My username: @{bot_account.username}\n'
                f'<b>Locale default:</> {html.bold(settings.DEFAULT_LOCALE)}.\n'
                f'<b>Available locales:</> {html.bold(", ".join(i18n.available_locales) or settings.DEFAULT_LOCALE)}.\n'
                f'<b>Timezone default:</> {html.bold(settings.DEFAULT_TIMEZONE)}.\n'
                f'<b>Start time:</> {html.code(_start_time)}.\n'
            )
        )


async def _on_shutdown(dispatcher: Dispatcher, bots: list[Bot], _: I18n.gettext):
    _working_time = str(dt.datetime.utcnow() - settings.START_TIME).split('.')[0]
    for bot in bots:
        await malling_message.text(
            bot=bot,
            chat_ids=settings.SUPERUSERS_TELEGRAM_ID,
            message_text=_(
                '<b>Bot stopped!</>\n'
                f'<b>Time stopped:</> {dt.datetime.now(ZoneInfo(settings.DEFAULT_TIMEZONE))}\n'
                f'<b>Working time:</> {_working_time}\n\n'
            )
        )

        try:
            await bot.close()
        except Exception as ex:
            continue
    await dispatcher.fsm.storage.close()


if __name__ == '__main__':

    # Create dirs.
    if not os.path.isdir(settings.TMP_DIR):
        os.mkdir(settings.TMP_DIR)
    if not os.path.isdir(settings.LOGS_DIR):
        os.mkdir(settings.LOGS_DIR)
    if not os.path.isdir(f'{settings.LOGS_DIR}/{settings.START_TIME}'):
        os.mkdir(f'{settings.LOGS_DIR}/{settings.START_TIME}')

    loggers.setup()

    # List bots.
    bots = [
        Bot(token=settings.TELEGRAM_BOT_API_TOKEN, parse_mode='HTML')
    ]

    dispatcher = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT, isolate_events=False)

    i18n = I18n(path=settings.LOCALES_DIR, default_locale=settings.DEFAULT_LOCALE, domain=settings.I18N_DOMAIN)

    # Data available in the workflow.
    bot_data = {
        '_': i18n.gettext, 'i18n': i18n,
    }

    # Registration of logic before launching bots.
    dispatcher.startup.register(_on_startup)

    # Registering logic before completing bots.
    dispatcher.shutdown.register(_on_shutdown)

    # Registration middlewares, filters, handlers.
    middlewares.setup(dispatcher, i18n=i18n)
    filters.setup(dispatcher)
    handlers.setup(dispatcher)

    try:
        # Start long polling.
        dispatcher.run_polling(*bots, **bot_data)
    except (KeyboardInterrupt, SystemExit):
        logging.warning('Bot stopped!')
    except Exception as ex:
        logging.exception(ex)
