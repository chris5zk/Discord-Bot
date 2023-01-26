from configparser import ConfigParser
import bot

if __name__ == '__main__':
    config = ConfigParser()
    config.read('config.ini')

    TOKEN = config['BOT']['TOKEN']
    FULL = config['LOG']['FULL']
    CHAT = config['LOG']['CHAT']

    bot.run_discord_bot(TOKEN, FULL, CHAT)
