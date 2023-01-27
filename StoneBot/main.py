from configparser import ConfigParser
from config import make_config_file
from bot import run_discord_bot
import bot


if __name__ == '__main__':
    # build the config.ini
    make_config_file()
    config = ConfigParser()
    config.read('config.ini')

    TOKEN = config['BOT']['TOKEN']
    FULL = config['LOG']['FULL']
    CHAT = config['LOG']['CHAT']

    run_discord_bot(TOKEN, FULL, CHAT)
