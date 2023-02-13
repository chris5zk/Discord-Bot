import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import date, timedelta, datetime


class MyTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='midnight', interval=1, backupCount=0):
        super().__init__(filename=filename, when=when, interval=interval, backupCount=backupCount, encoding="utf-8")
        self.namer = rotator_namer


def rotator_namer(filename):
    yesterday = (date.today() - timedelta(1)).isoformat()
    return filename.split('.log')[0] + '_' + yesterday + '.log'


async def log_message(msg):
    return f'```[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}][INFO ]{msg}```'
