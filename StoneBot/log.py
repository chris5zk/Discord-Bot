import logging
import logging.handlers


def full_log(path):
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename=path,
        encoding='utf-8',
        maxBytes=128 * 1024 * 1024,  # 128 MiB
        backupCount=24  # Rotate through 24 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def chat_log(path):
    logger = logging.getLogger('StoneBot')
    logger.setLevel(logging.DEBUG)

    handler = logging.handlers.RotatingFileHandler(
        filename=path,
        encoding='utf-8',
        maxBytes=128 * 1024 * 1024,  # 128 MiB
        backupCount=24  # Rotate through 24 files
    )

    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime} {name}][{levelname}] {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
