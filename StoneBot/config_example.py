"""
# config.ini
[BOT]
number = 1
name = Bot name
token = Bot TOKEN

[LOG]
full = log file path
chat = chat record file path
"""
from configparser import ConfigParser


def make_config_file():
    config = ConfigParser()

    config['BOT'] = {
        "NUMBER": 1,    # Number
        "NAME": ' ',    # Bot name
        "TOKEN": ' '    # Bot TOKEN
    }
    config['LOG'] = {
        "FULL": ' ',   # log file path
        "CHAT": ' '    # chat record file path
    }

    with open('config.ini', 'w') as f:
        config.write(f)
