import datetime as dt
from pathlib import Path

from environs import Env

START_TIME = dt.datetime.utcnow()

BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'
TMP_DIR = BASE_DIR / 'tmp'
LOGS_DIR = BASE_DIR / 'logs'

I18N_DOMAIN = 'messages'


env = Env()
env.read_env(f'{BASE_DIR}/.env')

APP_NAME = env('APP_NAME', 'bot')


TELEGRAM_BOT_API_TOKEN = env('TELEGRAM_BOT_API_TOKEN')
DEFAULT_LOCALE = env('DEFAULT_LOCALE')
DEFAULT_TIMEZONE = env('DEFAULT_TIMEZONE')
SUPERUSERS_TELEGRAM_ID = [int(_id) for _id in env('SUPERUSERS_TELEGRAM_ID').split() if _id.isdigit()]
LINK_TO_REPO = env('LINK_TO_REPO')
